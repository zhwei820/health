from django.shortcuts import render

from django.http import JsonResponse
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType


def index(request):
    '''
    健康检查
    :param request:
    :return:
    正常返回: 服务正常, 数据库正常, 缓存正常
    '''
    ret = {'code': 0, 'msg': 'ok'}
    _ = ContentType.objects.first()
    _ = cache.get('empty_value_test_key')
    return JsonResponse(ret)
