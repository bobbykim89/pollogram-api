from django.urls import path
from .views import (
    CommentListCreatePerPostAPIView,
    CommentDeleteAPIView,
    CommentLikeCreateAPIView,
    CommentUnlikeDestroyAPIView
)

urlpatterns = [
    path('<int:post_id>/', view=CommentListCreatePerPostAPIView.as_view(),
         name='comment-list-create-on-post'),
    path('<int:pk>/delete/', view=CommentDeleteAPIView.as_view(),
         name='comment-delete'),
    path('<int:pk>/like/', view=CommentLikeCreateAPIView.as_view(),
         name='comment-like'),
    path('<int:pk>/unlike/', view=CommentUnlikeDestroyAPIView.as_view(),
         name='comment-unlike')
]
