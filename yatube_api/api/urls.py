from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSets, FollowViewSet, GroupViewSets, PostViewSets

router = SimpleRouter()
router.register(r'posts', PostViewSets)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSets, basename='comment'
)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'groups', GroupViewSets)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
