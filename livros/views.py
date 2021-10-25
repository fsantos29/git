from .models import livro
from django.http import HttpResponse


def livros_view(request):
    livros = livro.objects.all()
    return HttpResponse(str(livros))

