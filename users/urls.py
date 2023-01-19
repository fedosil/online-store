from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', User_Login_View.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', User_Registration_View.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(User_Profile_View.as_view()), name='profile'),
    path('verification/<str:email>/<uuid:code>/', Email_Verification_View.as_view(), name='email_verification'),
]

