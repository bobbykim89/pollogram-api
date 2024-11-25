from django.urls import path
from .views import PostListCreateAPIView

urlpatterns = [
    path('', view=PostListCreateAPIView.as_view(), name='post-list-create')
]
