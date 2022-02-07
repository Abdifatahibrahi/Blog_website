from django.urls import path
from . import views
urlpatterns = [
    path("", views.StartingPageView.as_view(), name='starting-page'),
    path("posts", views.PostListView.as_view(), name='posts-page'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name='post-detail-page')
]


