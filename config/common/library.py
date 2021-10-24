from .response_code import *
from django.utils import timezone
from datetime import timedelta

JSON_CODE = "code"
JSON_MESSAGE = "message"
JSON_DATA = "data"


def common_serializer(code, data=None):
    json_data = dict()
    json_data[JSON_CODE] = code
    json_data[JSON_MESSAGE] = code_to_message(code)
    json_data[JSON_DATA] = data
    return json_data


def common_multi_serializer(code, data=None):
    json_data = dict()
    json_multi_data = dict()
    for key, value in data.items():
        json_multi_data[key] = value
    json_data[JSON_CODE] = code
    json_data[JSON_MESSAGE] = code_to_message(code)
    json_data[JSON_DATA] = json_multi_data
    return json_data


def get_now(): return timezone.localtime(timezone.now())


def get_after_day(d): return get_now() + timedelta(days=d)


def get_before_min(m): return get_now() + timedelta(seconds=(-60 * m))


def get_before_day(d): return get_now() + timedelta(days=(-1 * d))


def paging(request):
    page = int(request.GET['page']) - 1
    size = int(request.GET['size'])
    start_row = int(page) * int(size)
    end_row = (int(page) + 1) * int(size)
    return start_row, end_row
