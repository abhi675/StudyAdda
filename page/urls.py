from django.urls import path
from . import views
urlpatterns=[path('',views.index,name='index'),
path('payment/<int:price>/<course>',views.payment,name='payment'),]