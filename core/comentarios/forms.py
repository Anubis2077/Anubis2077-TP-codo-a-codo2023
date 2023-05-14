from django import forms
from django_comments.forms import CommentForm
from .models import Comentario

class ComentarioFormulario(CommentForm):
    titulo = forms.CharField(max_length=300)
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comentario
        fields = (
        'titulo',
        'comment',
        'owner',
        )

    def get_comment_model(self):
        return Comentario

    def get_comment_create_data(self, **kwargs):
        data = super().get_comment_create_data(**kwargs)
        data['titulo'] = self.cleaned_data['titulo']
        return data