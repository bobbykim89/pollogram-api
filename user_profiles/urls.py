from django.urls import path
from .views import UserProfileDetailAPIView, UserProfileCreateListAPIView, CurrentUserProfileAPIView

urlpatterns = [
    path('', view=UserProfileCreateListAPIView.as_view(),
         name='profile-create-list'),
    path('<int:pk>/', view=UserProfileDetailAPIView.as_view(), name='profile-detail'),
    path('current-user/', view=CurrentUserProfileAPIView.as_view(),
         name='current-user-profile')
]
