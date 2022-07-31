from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail

from .forms import EmailPostForm, ComentarioForm
from .models import Post


class PostListView(ListView):
    queryset = Post.publicadas.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/posts.html'


def detalhe_post(request, ano, mes, dia, post):
    template = 'blog/post/detalhe_post.html'
    post = get_object_or_404(
        Post,
        slug=post,
        status='publicadas',
        publicada__year=ano,
        publicada__month=mes,
        publicada__day=dia
    )

    comentarios = post.comentario.filter(ativo=True)
    novo_comentario = None

    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.post = post
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm()

    context = {
        'post': post,
        'comentarios': comentarios,
        'novo_comentario': novo_comentario,
        'comentario_form': comentario_form
    }

    return render(request, template, context)


def compartilhar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publicadas')
    template = 'blog/post/enviar_post.html'
    enviado = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            formulario_submetido = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            mensagem_cabecalho = f'{formulario_submetido["nome"]} recomenda você ler {post.titulo}'
            mensagem = f'Ler {post.titulo} no {post_url} \n\n {formulario_submetido["nome"]}' \
                       f' s comentario: {formulario_submetido["comentario"]}'

            send_mail(
                mensagem_cabecalho,
                mensagem,
                'samueldjangoex42@gmail.com',
                [formulario_submetido['email_destino']]
            )
            enviado = True
    else:
        form = EmailPostForm()

    context = {'post': post, 'form': form, 'enviado': enviado}

    return render(request, template, context)
