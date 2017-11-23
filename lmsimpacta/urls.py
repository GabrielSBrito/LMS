"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core.views import *

from django.contrib.auth.views import login, logout


urlpatterns = [

    url(r'^admin/',     admin.site.urls),
    url(r'^$',          index,                                     name="home" ),
    url(r'^matricula/', matricula,                                 name="matricula"),

    url(r'^entrar/',    login,   {"template_name":"login.html"},   name="login"),
    url(r'^sair/',      logout,  {"template_name":"index.html"},   name="logout"),



    url(r'^pagina_inicial_professor/', pagina_inicial_professor,   name="pagina_inicial_professor"),
        url(r'^perfil_professor/',         perfil_professor,           name="perfil_professor"),

    url(r'^subir_aula/',               subir_aula,                 name="subir_aula"),

    url(r'^boletim/',                  boletim,                    name="boletim"),
        url(r'^notas/',                    notas,                      name="notas"),

    url(r'^seleciona_turma_falta/',   seleciona_turma_falta,       name="seleciona_turma_falta"),    
        url(r'^faltas/',                   faltas,                     name="faltas"),

    url(r'^mensagens/',               mensagens,                   name="mensagens"), 


    url(r'^subir_atividades/',        subir_atividades,            name="subir_atividades"), 


]
