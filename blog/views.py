from django.shortcuts import render, HttpResponse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'post/list.html', {'posts': posts})

def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Publicación no encontrada")
    
    return render(request, 'post/detail.html', {'post':post})

@login_required
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #cd = form.cleaned_data
            #print(cd)
            post = form.save()
            messages.success(request, "Se creo el post con exito")
            return render(request, 'post/createpost.html', {'new_post':post})
    
    else:
        form = PostForm()
    
    return render(request, 'post/createpost.html', {'form': form})

    

