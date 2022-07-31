from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db import models


class PublicadasManager(models.Manager):
    def get_queryset(self):
        return super(PublicadasManager, self).get_queryset().filter(status='publicadas')


class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicadas', 'Publicadas'),
    )

    titulo = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='publicada')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    corpo = models.TextField()
    publicada = models.DateField(default=timezone.now)
    criada = models.DateTimeField(auto_now_add=True)
    atualizada = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')
    objetos = models.Manager()
    publicadas = PublicadasManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-publicada',)
        db_table = 'post'

    def get_absolute_url(self):
        return reverse(
            'blog:detalhe_post',
            args=[
                self.publicada.year,
                self.publicada.month,
                self.publicada.day,
                self.slug
            ]
        )

    def __str__(self):
        return f'{self.titulo}'


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentario')
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ('-criado',)
        db_table = 'comentarios'
