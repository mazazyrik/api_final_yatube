from django.urls import path

from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSets, GroupViewSets, PostViewSets

router = SimpleRouter()
router.register('posts', PostViewSets)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSets, basename='comment'
)
router.register('groups', GroupViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
