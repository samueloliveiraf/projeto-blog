from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    queryset = Post.publicadas.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/posts.html'


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
