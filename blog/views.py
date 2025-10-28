from django.shortcuts import render, redirect, get_object_or_404
from .models import MyPost

# READ
def post_list(request):
    posts = MyPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# CREATE
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        MyPost.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'post_form.html')

# UPDATE
def post_update(request, id):
    post = get_object_or_404(MyPost, id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')
    return render(request, 'post_form.html', {'post': post})

# DELETE
def post_delete(request, id):
    post = get_object_or_404(MyPost, id=id)
    post.delete()
    return redirect('post_list')
