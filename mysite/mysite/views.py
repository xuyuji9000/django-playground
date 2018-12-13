from django.http import HttpResponse
import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(json_handler)


def homepage(request):
    return HttpResponse('homepage')

def critical_log(request):
    logger.critical('Something went wrong!')
    return HttpResponse('critical_log')
