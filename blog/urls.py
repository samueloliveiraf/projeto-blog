from django.urls import path

from .feeds import UltimosPostsFeed
from . import views


app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/compartilhar-post/', views.compartilhar_post, name='compartilhar_post'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:post>/', views.detalhe_post, name='detalhe_post'),
    path('tag/<slug:tag_slug>/', views.lista_post, name='listar_post_by_tag'),
    path('feed/', UltimosPostsFeed(), name='post_feed'),
    path('post-buscar/', views.post_buscar, name='post_buscar'),
    path('', views.lista_post, name='listar_posts'),
]
