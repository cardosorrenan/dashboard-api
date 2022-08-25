from django.urls import path

from knox.views import LogoutView

from users.views import LoginView, RegisterAPI, RefreshToken, UserInfo

urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('register/', RegisterAPI.as_view(), name='user_register'),
    path('refresh/', RefreshToken.as_view(), name='user_refresh_token'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('me/', UserInfo.as_view(), name='user_info')
]