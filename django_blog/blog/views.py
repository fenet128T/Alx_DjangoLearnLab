from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import RegisterForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Post,Comment,Tag
from .forms import CommentForm
from django.views.generic import DetailView
from .forms import PostForm


# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


# ---------------- PROFILE ----------------
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")

    return render(request, "blog/profile.html")

# ---------------- LIST VIEW ----------------
class PostListView(ListView):
    """
    Displays all blog posts.
    Accessible to everyone.
    """
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]


# ---------------- DETAIL VIEW ----------------
class PostDetailView(DetailView):
    """
    Displays a single blog post.
    Accessible to everyone.
    """
    model = Post
    template_name = "blog/post_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

# ---------------- CREATE VIEW ----------------
class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows authenticated users to create posts.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        tags_string = form.cleaned_data['tags']
        tag_list = [tag.strip() for tag in tags_string.split(',') if tag.strip()]

        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            self.object.tags.add(tag)
        return response


# ---------------- UPDATE VIEW ----------------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows only the author to update their post.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.tags.clear()
        tags_string = form.cleaned_data['tags']
        tag_list = [tag.strip() for tag in tags_string.split(',') if tag.strip()]

        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            self.object.tags.add(tag)

        return response


# ---------------- DELETE VIEW ----------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows only the author to delete their post.
    """
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

   # ----------------- ADD COMMENT ---------------- 
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    return redirect('post-detail', pk=post.pk)

# ----------------- CREATE COMMENT ----------------
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post_id = self.kwargs['pk']  # get post id from URL
        post = get_object_or_404(Post, pk=post_id)
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()



# ----------------- UPDATE COMMENT ----------------
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# ----------------- DELETE COMMENT ----------------
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# ----------------- SEARCH VIEW ----------------
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.all()
    
# ----------------- TAG VIEW ----------------
class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = Tag.objects.get(name=self.kwargs['tag_name'])
        return self.tag.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
   