from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def seonghun_page(request):
    return render(
        request,
        'blog/seonghun.html',)
def about_rumi_page(request):
    return render(
        request,
        'blog/about_rumi.html',)
def pot_page(request):
    return render(
        request,
        'blog/about_rumi/PORTPORIO.html',)
def hansua_page(request):
    return render(
        request,
        'blog/hansua.html',)
def mbti_page(request):
    return render(
        request,
        'blog/hansua/mbti.html',)
def effort_page(request):
    return render(
        request,
        'blog/hansua/effort.html',)
def forest_page(request):
    return render(
        request,
        'blog/hansua/forest.html',)
def hobby_page(request):
    return render(
        request,
        'blog/hansua/hobby.html',)
def jihyun_page(request):
    return render(
        request,
        'blog/jihyun.html',)

def limdoyoung_page(request):
    return render(
        request,
        'blog/limdoyoung.html',)