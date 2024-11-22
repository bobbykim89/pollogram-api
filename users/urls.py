from django.urls import path
from .views import (
    SignupView,
    PasswordChangeView,
    CustomTokenObtainPairView,
    SignupAPIView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', view=SignupAPIView.as_view(), name='signup'),
    path('login/', view=CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', view=TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', view=PasswordChangeView.as_view(),
         name='change_password')
]
