from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login,name='login'),
    path('accept/',views.accept,name='accept'),
    path('adm/',views.adm,name='adm'),
    path('addcc/',views.addcc,name='addcc')
]