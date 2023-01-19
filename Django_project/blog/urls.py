from django.urls import path
from .	import views
urlpatterns =	[
    path('aa/',views.aa_page),
    path('<int:value>/',views.single_post_page),
    path('',views.index),
]
