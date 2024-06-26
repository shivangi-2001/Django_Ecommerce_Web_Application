from django.urls import path, include
from django.contrib.auth.views import LogoutView
from PROFILE.views import RegisterView, VerifyOTPView, Login, AccountProfile, get_user_id

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name="create_user"),
    path('auth/<int:pk>/verify_otp', VerifyOTPView.as_view(), name='verify_otp'),
    path('login', Login.as_view(), name='login'),
    path('auth/<str:pk>/accounts/profile', AccountProfile.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('get_user_id', get_user_id, name="get_user_id")
]