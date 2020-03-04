from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
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