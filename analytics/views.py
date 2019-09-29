from django.db.models import F
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from analytics.models import Claps, Referrers, PageCounts, UserAgents


def update_count(model, **filters):
    try:
        model.objects.filter(
            **filters
        ).update(
            count=F('count') + 1,
        )
    except ValueError:
        model.objects.create(**filters, count=1)


def access_control_allow_origin(f):
    def wrapper(request, *args, **kwargs):
        if request.method == 'OPTIONS':
            r = HttpResponse('')
            r['Access-Control-Allow-Origin'] = '*'
            r['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
            r['Access-Control-Allow-Headers'] = 'X-PINGARUNER'
            r['Access-Control-Max-Age'] = '1728000'
            r['Content-Length'] = '0'
            r['Content-Type'] = 'text/plain'
            return r

        r = f(request, *args, **kwargs)
        r['Access-Control-Allow-Origin'] = '*'
        return r
    return wrapper


@access_control_allow_origin
@require_POST
@csrf_exempt
def report(request):
    url = request.POST['url']

    referrer = request.POST.get('referrer')
    if referrer:
        update_count(Referrers, page_url=url, referrer=referrer)

    update_count(PageCounts, page_url=url)
    update_count(UserAgents, user_agent=request.META['HTTP_USER_AGENT'])

    return HttpResponse('ok')


@access_control_allow_origin
@require_GET
@csrf_exempt
def claps(request):
    try:
        return HttpResponse(str(Claps.objects.get(page_url=request.GET['url']).count))
    except Claps.DoesNotExist:
        return HttpResponse('0')


@access_control_allow_origin
@require_POST
@csrf_exempt
def clap(request):
    update_count(Claps, page_url=request.GET['url'])
    return HttpResponse('ok')
