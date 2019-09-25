from django.db.models import F
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from analytics.models import Claps, Referrers, PageCounts, UserAgents


@require_POST
@csrf_exempt
def report(request):
    url = request.POST['url']

    referrer = request.POST.get('referrer')
    if referrer:
        Referrers.objects.update_or_create(
            page_url=url,
            referrer=referrer,
            defaults=dict(count=F('counts') + 1),
        )

    PageCounts.objects.update_or_create(
        page_url=url,
        defaults=dict(count=F('counts')+1),
    )

    UserAgents.objects.update_or_create(
        page_url=url,
        user_agent=request.META['User-Agent'],
        defaults=dict(count=F('counts') + 1),
    )

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
        defaults=dict(count=F('counts')+1),
    )

    return HttpResponse('ok')
