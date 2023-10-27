from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    #path("register", views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('Registre/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', HomeView.as_view(), name='home' ),
    path('product/', ProductView.as_view(), name='home' ),
    path('store/', StoreView.as_view(), name='home' ),
    path('blank/', BlankView.as_view(), name='home' ),
    path('find/',FindView.as_view())
    

]