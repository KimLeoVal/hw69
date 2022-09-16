import json

from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView, CreateView

from webapp.forms import TestForm
from webapp.models import Test


def index_view(request):
    return render(request,'index.html')

@ensure_csrf_cookie

def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

def all_actions(request):
    body = json.loads(request.body)
    action = request.META.get('PATH_INFO').strip('/')
    a = str(body.get('a'))
    b = str(body.get('b'))
    if not a.isdigit():
        response = JsonResponse({'error': f'{a}  not integer'})
        response.status_code = 400
        return response
    if not b.isdigit():
        response = JsonResponse({'error': (f'{b} not integer')})
        response.status_code = 400
        return response
    if action=='add':
        c = int(a) + int(b)
        answer = {"answer": c}
        return JsonResponse(answer)
    if action=='subtract':
        c = int(a) - int(b)
        answer = {"answer": c}
        return JsonResponse(answer)
    if action=='multiply':
        c = int(a) * int(b)
        answer = {"answer": c}
        return JsonResponse(answer)
    if action=='divide':
        if int(b) == 0:
            response = JsonResponse({'error': (' zero division error')})
            response.status_code = 400
            return response
        else:
            c = int(a) / int(b)
            answer = {"answer": c}
            return JsonResponse(answer)

class TestView(ListView):
    model = Test
    template_name = 'index_test.html'
    context_object_name = 'test'

class CreateTest(CreateView):
    template_name = 'create.html'
    form_class = TestForm

    def form_valid(self, form):
        super().form_valid(form)

#
# def add_numbers(request):
#     body=json.loads(request.body)
#     a = body.get('a')
#     b = body.get('b')
#     if not a.isdigit():
#         response = JsonResponse({'error': f'{a}  not integer'})
#         response.status_code = 400
#         return response
#     if not b.isdigit():
#         response = JsonResponse({'error': (f'{b} not integer')})
#         response.status_code = 400
#         return response
#     c = int(a)+int(b)
#     answer = {"answer": c}
#     return JsonResponse(answer)
#
# def subtract_numbers(request):
#     body = json.loads(request.body)
#     a = body.get('a')
#     b = body.get('b')
#     if not a.isdigit():
#         response = JsonResponse({'error': f'{a}  not integer'})
#         response.status_code = 400
#         return response
#     if not b.isdigit():
#         response = JsonResponse({'error': (f'{b} not integer')})
#         response.status_code = 400
#         return response
#     c = int(a)-int(b)
#     answer = {"answer": c}
#     return JsonResponse(answer)
#
# def multiply_numbers(request):
#     body = json.loads(request.body)
#     a = body.get('a')
#     b = body.get('b')
#     if not a.isdigit():
#         response = JsonResponse({'error': f'{a}  not integer'})
#         response.status_code = 400
#         return response
#     if not b.isdigit():
#         response = JsonResponse({'error': (f'{b} not integer')})
#         response.status_code = 400
#         return response
#     c = int(a)*int(b)
#     answer = {"answer": c}
#     return JsonResponse(answer)
#
# def divide_numbers(request):
#     body = json.loads(request.body)
#     a = body.get('a')
#     b = body.get('b')
#     if not a.isdigit():
#         response = JsonResponse({'error': f'{a}  not integer'})
#         response.status_code = 400
#         return response
#     if int(b)==0:
#         response = JsonResponse({'error': (' zero division error')})
#         response.status_code = 400
#         return response
#     if not b.isdigit():
#         print(b)
#         response = JsonResponse({'error': (f'{b} not integer')})
#         response.status_code = 400
#         return response
#
#     c = int(a)/int(b)
#     answer = {"answer": c}
#     return JsonResponse(answer)
#
#














