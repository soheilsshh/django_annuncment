from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('login',views.login, name = 'login'),
    path('signin',views.signin, name = 'signin'),
    path('profile',views.profile,name = 'profile'),
    path('add_ads',views.add_ads,name="add_ads"),
    path('post_list',views.post_list,name='post_list'),
    path('update/<int:id>',views.update_ad,name='update_ad'),
    path('detile/<int:id>',views.detile,name='detile')
]

