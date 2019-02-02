from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegisterAPIView, PostListView, PostDetailsView, post_interactions

app_name = 'api'

# TODO: Move from regex to paths

urlpatterns = [
    url(r'^register/?$', RegisterAPIView.as_view(), name='register'),
    url(r'^login/?$', obtain_jwt_token, name='login'),
    url(r'posts/?$', PostListView.as_view(), name='posts_list'),
    url(r'posts/(?P<pk>[0-9]*)/?$', PostDetailsView.as_view(), name='post_details'),
    url(r'posts/(?P<pk>[0-9]*)/(?P<interaction>[\w\-]+)/?$', post_interactions, name='post_interactions')
]