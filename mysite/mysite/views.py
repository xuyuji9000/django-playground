from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def homepage(request):
    return HttpResponse('homepage')

def critical_log(request):
    logger.critical('Something went wrong!')
    return HttpResponse('critical_log')
