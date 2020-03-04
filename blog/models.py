from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    """
        Titulo
        Conteudo
        data-de-publicacao
        data-de-edicap
        imagem
        Autor
    """
    titulo = models.CharField('Título', max_length=200)
    conteudo = models.TextField('Conteúdo')
    data_pub = models.DateTimeField('Data de Publicação', auto_now=True)
    data_edi = models.DateTimeField('Data de Atualização', auto_now_add=True)
    imagem = models.ImageField('Imagem', upload_to='imagens')

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
