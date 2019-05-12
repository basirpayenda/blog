from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import BlogForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(ListView):
    queryset = BlogPost.objects.order_by('-created_at')
    template_name = "blogs/home.html"
    context_object_name = 'queryset'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*kwargs)
        context['latest_post'] = BlogPost.objects.order_by("-created_at")[:5]
        return context


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/blog-detail.html'

    def get_object(self):
        slug = self.kwargs.get('title_slug')
        return get_object_or_404(BlogPost, slug=slug)


class PostCreateView(SuccessMessageMixin, CreateView):
    model = BlogPost
    template_name = 'blogs/blog-form.html'
    fields = ['title', 'content', 'image']
    success_message = 'Post added successfully!'


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'blogs/blog-update.html'
    fields = ['title', 'content', 'image']
    success_message = 'Post updated successfully!'

    def get_object(self):
        slug = self.kwargs.get('title_slug')
        return get_object_or_404(BlogPost, slug=slug)


class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = 'blogs/blog-delete.html'
    success_message = 'Post deleted successfully!'
    success_url = "/"

    def get_object(self):
        slug = self.kwargs.get('title_slug')
        return get_object_or_404(BlogPost, slug=slug)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)
