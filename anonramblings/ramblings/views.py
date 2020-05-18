from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from .models import Post
from .forms import PostForm

from datetime import datetime, timedelta


def index(request):

    three_days_ago = datetime.utcnow() - timedelta(days=3)

    post_list = Post.objects.filter(
        is_approved=True, is_deleted=False)

    if 'q' in request.GET:
        post_list = post_list.filter(
            title__icontains=request.GET.get("q")) | post_list.filter(
            body__icontains=request.GET.get("q"))

    if 'trending' in request.path:
        post_list = post_list.filter(
            created_at__gt=three_days_ago, parent=None).order_by("-comment_count")
    else:
        post_list = post_list.order_by("-id")


    paginator = Paginator(post_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "base.html", {'page_obj': page_obj})


def post(request):
    reply_to = request.GET.get("reply_to")

    # is it a reply?
    if reply_to:
        try:
            parent_post = Post.objects.get(permlink=reply_to)
        except Post.DoesNotExist:
            raise Http404
    else:
        parent_post = None

    if request.method == 'POST':
        form = PostForm(request.POST, )

        if not form.is_valid():
            return render(request, "post.html", {"form": form})
        instance = form.save(commit=False)
        instance.parent = parent_post
        instance.save()
        if reply_to:
            parent_post.comment_count = parent_post.get_descendants().count()
            parent_post.save()
        return redirect('/thanks/?permlink=%s' % instance.permlink)
    else:
        initial = {}
        if parent_post:
            initial.update({"title": "Re: %s" % parent_post.title})
        form = PostForm(initial=initial)

    return render(request, "post.html", {"form": form, "reply_to": reply_to})


def detail(request, permlink):
    try:
        post = Post.objects.get(permlink=permlink, is_deleted=False)
    except Post.DoesNotExist:
        raise Http404

    descendants = post.get_descendants().filter(is_deleted=False)

    return render(request, "detail.html", {"post": post, "descendants": descendants})


def about(request):
    return render(request, "about.html")


def thanks(request):
    return render(request, "thanks.html")