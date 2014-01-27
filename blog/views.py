from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm

from blog.models import Comment
from blog.models import Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']


def main(request):
    """Main listing."""
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 2)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': posts})


def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    # now return the rendered template
    return render(request, 'blog/post.html', d)#{'post': post})


def add_comment(request, slug):
    """Add a new comment."""
    #print("looool")
    p = request.POST

    if  p["content"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(slug=slug))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blog.views.post", args=[slug]))

