from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# InputForm

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    template_name = "home.html"
    model = Post
    #ordering = ["-id"]
    ordering = ["-post_date"]

class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Post

class AddPostView(CreateView):
    template_name = "add_post.html"
    model = Post
    form_class = PostForm
    #fields = '__all__'
    
# def home_view(request):
#     context = {}
#     context['form'] = InputForm()
#     return render(request, "test.html", context)

# test.html view
# class home_view(View):
#     def post(self, request):
#         context = {}
#         context['form'] = InputForm()
#         return render(request, "test.html", context)


class  UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    #fields = ['title', 'title_tag', 'body']
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_confirmation.html' 
    success_url = reverse_lazy('home')
