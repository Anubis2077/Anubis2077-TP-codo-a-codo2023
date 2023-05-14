from django.db import models
from django.db import models
from django_comments.abstracts import CommentAbstractModel
from core.accounts.models import User

class Comentario(CommentAbstractModel):
    titulo = models.CharField(max_length=300)
    comment = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    class Meta:
        ordering = ['-submit_date']
