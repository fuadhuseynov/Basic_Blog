from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm


#POST_LIST view
def post_list(request):
    queryset_list = Post.objects.all()
    page_request_var = "page"
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, 'posts/post_list.html', {"object_list":queryset, "page_request_var":page_request_var})


#POST_DETAIL view
def post_detail(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {"object":instance})


#POST_CREATE view
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'posts/post_form.html', {"form":form})


#POST_UPDATE view
def post_update(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Edited!")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'posts/post_form.html', {"object":instance, "form":form})


#POST_DELETE view
def post_delete(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:post_list")














