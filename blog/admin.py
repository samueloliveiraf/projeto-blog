from django.contrib import admin
from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicada', 'status')
    list_filter = ('titulo', 'criada', 'autor', 'publicada')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'post', 'criado', 'ativo')
    list_filter = ('ativo', 'criado', 'atualizado')
    search_fields = ('nome', 'corpo', 'email')
