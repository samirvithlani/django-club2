from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Blog
from .forms import BlogCreateionForm
# Create your views here.
#class based function

class BlogCreateView(CreateView):
    model = Blog
    template_name ="blog/blog_create.html"
    success_url ="/blog/create"
    form_class = BlogCreateionForm
    
    # def get_context_data(self, **kwargs):
    #form_valid

class BlogListView(ListView):  
    template_name = "blog/blog_list.html"
    model = Blog
    context_object_name = "blogs"
    #get_queryset

class BlogDeleteView(DeleteView):
    template_name = "blog/blog_delete.html"
    model = Blog
    success_url = "/blog/list"
    
    #get
    #get_context_data --> id
    

class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    success_url = "/blog/list"
    template_name = "blog/blog_update.html"    


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"    
    context_object_name = "blog"  
    