from django.shortcuts import render, get_object_or_404
from .models import Post


def listar_posts(request):
    posts = Post.publicadas.all()
    context = {'posts': posts}
    return render(request, 'blog/post/posts.html', context)


def detalhe_post(request, ano, mes, dia, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='publicadas',
        publicada__year=ano,
        publicada__month=mes,
        publicada__day=dia
    )
    context = {'post': post}
    return render(request, 'blog/post/detalhe_post.html', context)
