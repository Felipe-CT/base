from django.urls import path
from .views import LoginView, login, logout, Home

app_name = 'acceso'

urlpatterns = [
    path('', LoginView.as_view(), name='acceso' ),
    path('home/', Home, name='home' ),
    path('login/', login, name='login' ),
    path('logout/', logout, name='logout' ),
]
