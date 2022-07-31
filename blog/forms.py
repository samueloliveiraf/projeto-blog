from django import forms
from .models import Comentario


class EmailPostForm(forms.Form):
    nome = forms.CharField(max_length=150)
    email = forms.EmailField()
    email_destino = forms.EmailField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = (
            'nome',
            'email',
            'corpo'
        )
