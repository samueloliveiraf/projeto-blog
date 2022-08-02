from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/compartilhar-post/', views.compartilhar_post, name='compartilhar_post'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:post>/', views.detalhe_post, name='detalhe_post'),
    # path('', views.PostListView.as_view(), name='listar_posts'),
    path('', views.post_list, name='listar_posts'),
    path('tag/<slug:tag_slug>/', views.post_list, name='listar_post_by_tag'),
]
