from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.listar_posts, name='listar_posts'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:post>/', views.detalhe_post, name='detalhe_post'),
]
