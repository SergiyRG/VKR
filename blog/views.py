from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.utils import timezone
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView )
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.


class PostListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    ordering = ['-created_date']
    model = Post



class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    model = Post


def create_post(request):
    if request.method == 'POST':
        titulli = request.POST.get('title')
        permbajtja = request.POST.get('text')
        postim = Post(title=titulli, text=permbajtja, author=request.user)
        postim.save()
        messages.success(request, f'Публикация была успешно добавлена')
        return redirect('blogs:post_list')
    return render(request, 'blog/create_post.html')

def update_post(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Post, id = id)
 
    # pass the object as instance in form
    form = PostForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/blog/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, 'blog/update_post.html', context)

def delete_post(request, id):
    Post(id = id).delete()
    return redirect('blogs:post_list')