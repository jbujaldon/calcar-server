from authentication.views import AccessTokenView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('auth/token/', AccessTokenView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh')
]