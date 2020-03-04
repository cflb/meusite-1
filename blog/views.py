from django.shortcuts import render
from blog.models import Post

# Create your views here.
def lista_noticias(request):

    lista_de_posts = Post.objects.all()
    
    contexto = {
        'lista_de_posts': lista_de_posts
    }
    return render(request, 'lista_noticias.html', contexto)
