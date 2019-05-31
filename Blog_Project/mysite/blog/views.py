from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment, Post_Like, Comment_Like, User
from django.utils import timezone
from blog.forms import PostForm, CommentForm, UserCreateForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login, logout
User = get_user_model()


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("userlogin")
    template_name = "signup.html"

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
     login_url = '/userlogin/'
     redirect_field_name = 'blog/post_detail.html'

     form_class = PostForm

     model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/userlogin/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


def my_posts_list(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=logged_in_user).order_by('-created_date')
    return render(request, 'blog/my_post_list.html', {'posts': logged_in_user_posts})


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')



#######################################
## Functions that require a pk match ##
#######################################


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.author = request.user
    post.save()
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
       

@login_required
def post_like(request, pk):
    postid = get_object_or_404(Post, pk=pk)
    like = Post_Like()        
    like.post = postid
    like.author = request.user
    flag = False
    for li in Post_Like.objects.all():
       if li.post == like.post :
          if li.author == like.author :
             flag = True
             break

    if flag == False:
       like.save()
       like.like_post()

    return redirect('post_detail', pk=like.post.pk)     

@login_required
def comment_like(request, pk):
    commentid = get_object_or_404(Comment, pk=pk)
    like = Comment_Like()        
    like.comment = commentid
    like.author = request.user
    flag = False
    for li in Comment_Like.objects.all():
       if li.comment == like.comment :
          if li.author == like.author :
             flag = True
             break
             
    if flag == False:
       like.save()
       like.like_comment()

    return redirect('post_detail', pk=commentid.post.pk)
   