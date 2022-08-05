from django.template.defaultfilters import truncatewords
from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post


class UltimosPostsFeed(Feed):
    title = 'Meu Blog'
    link = reverse_lazy('blog:listar_posts')
    descricao = 'Novo posto do meu Blog'

    def items(self):
        return Post.publicadas.all()[:3]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return truncatewords(item.corpo, 30)
