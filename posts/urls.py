from django.urls import path
from .views import PostListCreateAPIView, PostDetailDeleteAPIView, PostLikeCreateAPIView, PostUnlikeDestroyAPIView

urlpatterns = [
    path('', view=PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>/', view=PostDetailDeleteAPIView.as_view(),
         name='post-detail-delete'),
    path('<int:pk>/like/', view=PostLikeCreateAPIView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', view=PostUnlikeDestroyAPIView.as_view(), name='post-unlike')
]
