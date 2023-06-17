from django.urls import path
from users.views import register, user_login, user_logout


app_name = 'users'

urlpatterns = [
    path('', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
