from django.db.models import F
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from analytics.models import Claps, Referrers, PageCounts, UserAgents


@require_POST
@csrf_exempt
def report(request):
    url = request.POST['url']

    def update_count(model, **filters):
        try:
            model.objects.filter(
                **filters
            ).update(
                count=F('count') + 1,
            )
        except ValueError:
            model.objects.create(**filters, count=0)

    referrer = request.POST.get('referrer')
    if referrer:
        update_count(Referrers, page_url=url, referrer=referrer)

    update_count(PageCounts, page_url=url)
    update_count(UserAgents, user_agent=request.META['HTTP_USER_AGENT'])

    return HttpResponse('ok')


@require_GET
@csrf_exempt
def claps(request):
    try:
        return HttpResponse(str(Claps.objects.get(page_url=request.GET['url']).count))
    except Claps.DoesNotExist:
        return HttpResponse('0')


@require_POST
@csrf_exempt
def clap(request):
    Claps.objects.update_or_create(
        page_url=request.GET['url'],
        defaults=dict(count=F('count')+1),
    )

    return HttpResponse('ok')
