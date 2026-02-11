from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_view, 
    profile_view, 
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    CommentUpdateView,
    CommentDeleteView,
    SearchResultsView, 
    TagPostListView
)
from .views import PostByTagListView


urlpatterns = [
    # ---------------- AUTH URLs ----------------
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),

# ---------------- POST URLs ----------------
     path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comment URLs
    path("post/<int:pk>/comments/new/", add_comment, name="add-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

 # ---------------- SEARCH & TAG URLs ----------------
    path('search/', SearchResultsView.as_view(), name='search'),
path('tags/<str:tag_name>/', TagPostListView.as_view(), name='tag-posts'),



    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),


]
