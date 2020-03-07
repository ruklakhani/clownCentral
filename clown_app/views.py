from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import PostForm
from .models import Post

class Home(ListView):
    model = Post 

    def get(self, request):
        posts = self.get_queryset().all()
        return render(request, 'home.html', {'posts': posts})

class AddPost(CreateView):
    model = Post 
    form_class = PostForm
    template_name = "add_post.html"

class ShowPost(DetailView):
    model = Post
    def get(self,request,slug):
        post = self.get_queryset().get(slug__iexact=slug)
        return render(request,"show_post.html",{'post':post})

class EditPost(UpdateView):
    model = Post 
    form_class = PostForm
    template_name = "edit_post.html"

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if not post.posted_by == self.request.user:
            return redirect(post)
        return super(EditPost, self).dispatch(request, *args, **kwargs)

class DeletePost(UpdateView):
    model = Post 
    form_class = PostForm
    template_name = "delete_post.html"

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if not post.posted_by == self.request.user:
            return redirect(post)
        return super(DeletePost, self).dispatch(request, *args, **kwargs)