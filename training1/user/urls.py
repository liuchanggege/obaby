from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$',views.login),
    url(r'^Redirect1$',views.Redirect1),
    url(r'^Redirect2$',views.Redirect2),
    url(r'^test$',views.Redirect2),
    url(r'^testPost$',views.testPost),
]
