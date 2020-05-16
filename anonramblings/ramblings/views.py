from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from .models import Post
from .forms import PostForm


def index(request):
    post_list = Post.objects.filter(
        is_approved=True, is_deleted=False).order_by("-id")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "base.html", {'page_obj': page_obj})


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if not form.is_valid():
            return render(request, "post.html", {"form": form})
        instance = form.save()
        if form.is_valid():
            return redirect('/thanks/?permlink=%s' % instance.permlink)
    else:
        form = PostForm()

    return render(request, "post.html", {"form": form})


def detail(request, permlink):
    try:
        post = Post.objects.get(permlink=permlink, is_deleted=False)
    except Post.DoesNotExist:
        raise Http404

    return render(request, "detail.html", {"post": post})


def about(request):
    return render(request, "about.html")


def thanks(request):
    return render(request, "thanks.html")