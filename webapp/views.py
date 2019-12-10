from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from . import util


# Create your views here.


def index(request):
    context = {}
    if request.method == 'POST':
        context = util.detectTrafficSign(request)
    context['title'] = 'Trang chủ'
    return render(request, 'index.html', context=context)
