from django.db import models
from django.shortcuts import render
from datetime import date

from django.views.generic.detail import DetailView
from .models import Post, Author, Tag

from django.views.generic import ListView
from .forms import CommentForm

from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.



def get_date(post):
    return post['date']


# def starting_page(request):
#     sorted_posts = sorted(all_posts, key=get_date)
#     latest_posts = sorted_posts[-3:]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("date")[:3]
    
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class PostListView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    

# def posts(request):
#     latest_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html",{
#         "all_posts" : latest_posts
#     })
    

class SinglePostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        context['form_comment']= CommentForm()
        return context

# def post_detail(request, slug):
#     mypost = Post.objects.get(slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         "post": mypost
#     })

class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "form_comment": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }

        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "form_comment": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post-detail.html', context)
   
