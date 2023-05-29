from django.urls import path
from rest_framework import routers
from .views import PostViewSet, like_post, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    path('posts/', PostViewSet.as_view({'get': 'list'}), name='post-list'),
    path('like/<int:pk>/', like_post, name='like_post'),
]
