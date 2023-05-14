from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render, redirect

from core.marketplace.models import Product
from .forms import CommentForm
from django_comments.models import Comment
from django_comments.views.comments import post_comment
from .models import Comentario




def CommentView(request, slug):
    product = get_object_or_404(Product, slug=slug)
    content_type = ContentType.objects.get_for_model(product)
    comments = Comment.objects.filter(content_type=content_type, object_pk=product.pk, is_public=True)

    form = CommentForm()  # Crear el form antes del if

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content_type = content_type
            new_comment.object_slug = product.slug
            new_comment.save()
            form = CommentForm()  # Reiniciar el form

    for comment in comments:
        print(comment.comment)

    return render(request, 'components/comentariosypreguntas.html', {'product': product, 'comments': comments, 'form': form})


