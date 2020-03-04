from django.urls import path
from .views import lista_noticias

urlpatterns = [
    path('lista_noticias/', lista_noticias),
]


"""
blog/
    lista-noticias/
    nova-noticias/
    detalhes/1/
    remover/
    modificar/

    C-REATE
    R-EAD (ALL - DETAIL)
    U-PDATE
    D-ELETE
"""