from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark

# Create your views here.
def book_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'book_list.html', {'bookmarks':bookmarks})

def add(request):
    return render(request, 'add.html')

def book_create(request):
    new_site = Bookmark()
    new_site.site_name = request.POST['site_name']
    new_site.url = request.POST['url']
    new_site.save()
    return redirect('book_list')

def book_delete(request, id):
    delete_site = Bookmark.objects.get(id=id)
    delete_site.delete()
    return redirect('book_list')