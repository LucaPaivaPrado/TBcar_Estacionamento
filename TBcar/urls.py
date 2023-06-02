"""TBcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, Registrar, cadastroCliente, cadastroVeiculo, cadastroTabela, cadastroRotativo,\
    cadastroMensalista, cadastroMarca,listagemCliente, listagemVeiculo, listagemTabela, listagemMarcas,\
    listagemMensalista, listagemRotativo, altera_cliente, altera_veiculo, altera_tabela, exclui_cliente,\
    exclui_veiculo, exclui_marca, altera_rotativo, altera_marca, altera_mensalista, exclui_mensalista,\
    exclui_rotativo

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name= 'url_registrar'),
    #path('captcha/', include('captcha.urls')),
    path('', home, name='url_principal'),
    path('cadastroCliente/', cadastroCliente, name='url_cadastro_cliente'),
    path('cadastroVeiculo/', cadastroVeiculo, name='url_cadastro_veiculo'),
    path('cadastroMarca/', cadastroMarca, name='url_cadastro_marca'),
    path('cadastroTabela/', cadastroTabela, name='url_cadastro_tabela'),
    path('cadastroMensalista/', cadastroMensalista, name='url_cadastro_mensalista'),
    path('cadastroRotativo/', cadastroRotativo, name='url_cadastro_rotativo'),
    path('listagemCliente/', listagemCliente, name='url_listagem_cliente'),
    path('listagemVeiculo/', listagemVeiculo, name='url_listagem_veiculo'),
    path('listagemTabela/', listagemTabela, name='url_listagem_tabela'),
    path('listagemMensalista/', listagemMensalista, name='url_listagem_mensalista'),
    path('listagemRotativo/', listagemRotativo, name='url_listagem_rotativo'),
    path('listagemMarcas/',listagemMarcas, name='url_listagem_marcas'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('altera_mensalista/<int:id>/', altera_mensalista, name='url_altera_mensalista'),
    path('altera_rotativo/<int:id>/', altera_rotativo, name='url_altera_rotativo'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculo'),
    path('altera_tabela/<int:id>/', altera_tabela, name='url_altera_tabela'),
    path('altera_marca/<int:id>/', altera_marca, name='url_altera_marca'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('exclui_marca/<int:id>/', exclui_marca, name='url_exclui_marca'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)