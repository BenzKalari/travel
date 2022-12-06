from . import views
from django.urls import path


urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('sub/',views.sub,name='subtraction'),
    # path('div/',views.divi,name='divition'),
    # path('mul/',views.multi,name='multi'),
    #


]
