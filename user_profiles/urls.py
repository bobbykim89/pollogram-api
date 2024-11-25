from django.urls import path
from .views import UserProfileDetailAPIView, CurrentUserProfileAPIView, UserProfileListAPIView, CurrentUserUpdateProfilePictureAPIView, UserProfileCreateFollowAPIView

urlpatterns = [
    path('', view=UserProfileListAPIView.as_view(),
         name='profile-list'),
    path('current-user/', view=CurrentUserProfileAPIView.as_view(),
         name='current-user-profile'),
    path('current-user/profile-image/',
         view=CurrentUserUpdateProfilePictureAPIView.as_view(), name='update-profile-image'),
    path('<int:pk>/', view=UserProfileDetailAPIView.as_view(), name='profile-detail'),
    path('<int:pk>/follow/', view=UserProfileCreateFollowAPIView.as_view(),
         name='follow-profile')
]
