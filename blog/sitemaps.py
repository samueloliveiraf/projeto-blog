from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreg = 'weekly'
    prioruty = 0.9

    def items(self):
        return Post.publicadas.all()

    def lastmod(self, obj):
        return obj.atualizada
