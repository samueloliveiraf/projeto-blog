from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='listar_posts'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:post>/', views.detalhe_post, name='detalhe_post'),
]
