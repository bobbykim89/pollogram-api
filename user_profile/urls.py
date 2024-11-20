from django.urls import path
from views import SignupView, LoginView, UpdatePasswordView

urlpatterns = [
    path('signup/', view=SignupView.as_view(), name='signup'),
    path('login/', view=LoginView.as_view(), name='login'),
    path('change-password', view=UpdatePasswordView.as_view(), name='update-password')
]
