from django.urls import path
from .	import views
urlpatterns =	[
    path('seonghun/',views.seonghun_page),
    path('hansua/',views.hansua_page),
    path('jihyun/',views.jihyun_page),
    path('limdoyoung/',views.limdoyoung_page),
    path('',views.index), 
    path('hansua/mbti/',views.mbti_page),
    path('hansua/forest/',views.forest_page),
    path('hansua/hobby/',views.hobby_page),
    path('hansua/effort/',views.effort_page),
    path('about_rumi/',views.about_rumi_page),
    path('about_rumi/PORTPORIO/',views.pot_page),
]
