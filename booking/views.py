
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def toJSON(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')
def student_view(request) :
    rst = {}
    rst['msg'] = "hello"
    if request.method == 'GET':
        return toJSON(rst, 200)
    elif request.method == 'POST':
        rst['method'] = "POST"
        return toJSON(rst, 200)
def student_detail_view(request, id) :
    rst = {}
    rst['msg'] = "hello"
    rst['id'] = id
    return toJSON(rst, 200)
# Create your views here.
