from django.utils.safestring import mark_safe
from django.db.models import Count
from django import template

import markdown

from ..models import Post


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.publicadas.count()


@register.inclusion_tag('blog/post/ultimos_posts.html')
def ver_ultimos_posts(count=3):
    ultimos_posts = Post.publicadas.order_by('-publicada')[:count]
    return {'ultimos_posts': ultimos_posts}


@register.simple_tag
def posts_mais_comentados(count=3):
    return Post.publicadas.annotate(
        total_comentarios=Count('comentario')
    ).order_by('-total_comentarios')[:count]


@register.filter(name='markdown')
def markdown_formatacao(texto):
    return mark_safe(markdown.markdown(texto))

