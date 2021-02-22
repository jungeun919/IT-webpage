from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def board(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)
    return render(request, 'post.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.content = request.POST['content']
    new_post.save()
    return redirect('detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    update_post.content = request.POST['content']
    update_post.save()
    return redirect('detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('board')

def comment_new(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.co_writer = request.user
            comment.post = post
            comment.save()
            return redirect('/qna/' + str(post.id))
    else:
        form = CommentForm()
        return render(request, 'comment_new.html', {"form":form})

def comment_update(request, comment_id):
    cur_comment = get_object_or_404(Comment, pk=comment_id)
    post = cur_comment.post

    if request.method == 'POST':
        form = CommentForm(request.POST, instance= cur_comment)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.author = request.user
            comment.save()
            return redirect('/qna/' + str(post.id))
    else:
        form = CommentForm(instance=cur_comment)
    return render(request, 'comment_update.html', {'form': form})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.co_writer:
        return redirect('/qna/' + str(comment.post.id))
    else:
        comment.delete()
    return redirect('/qna/' + str(comment.post.id))