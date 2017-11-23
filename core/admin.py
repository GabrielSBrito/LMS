from django.contrib import admin

from core.models import *

from django.contrib.auth.admin import UserAdmin
from django import forms
from random import randint

# Register your models here.
# ----------------------------------------ALUNO
def testara_Aluno(n):
    lista = []
    contexto = Usuario.objects.all()
    for x in contexto:
        lista.append(x.ra)
    while n in lista:
        n = randint(100000,199999)
    return n   

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso','celular')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'
        n = randint(100000,199999)
        ra_unico = testara_Aluno(n)
        user.ra = ra_unico        
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email', 'nome', 'curso','celular')
        
class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm


class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso')
    list_filter = ('perfil','curso')
    fieldsets = ( (None, {'fields': ('email', 'nome', 'curso','celular')}),)
    add_fieldsets = (
        (None, {
            'fields': ( 'email', 'nome', 'curso','celular')

            } ),
             
         )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

#-----------------------------------------PROFESSOR
def testara_Professor(n):
    lista = []
    contexto = Usuario.objects.all()
    for x in contexto:
        lista.append(x.ra)
    while n in lista:
        n = randint(100000,199999)
    return n   

class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('ra','email', 'nome','apelido','curso')

    def save(self, commit=True):
        user = super(NovoProfessorForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'P'
        n = randint(100000,199999)
        ra_unico = testara_Professor(n)
        user.ra = ra_unico        
        if commit:
            user.save()
        return user

class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('email', 'nome', 'apelido','curso')
        
class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm


class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm
    list_display = ('ra', 'nome','apelido','curso')
    list_filter = ('perfil','curso')
    fieldsets = ( (None, {'fields': ('email', 'nome','apelido','curso')}),)
    add_fieldsets = (
        (None, {
            'fields': ( 'email', 'nome','apelido','curso')

            } ),
             
         )
    search_fields = ('email',)
    ordering = ('nome',)
    filter_horizontal = ()    

# ----------------------------------------CURSO
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo','carga_horaria')
    list_filter = ('tipo',)

# ----------------------------------------GRADECURRICULAR  

class NovoGradeCurricularForm(forms.ModelForm):
    class Meta:
        model = GradeCurricular
        fields = ('curso', 'ano','semestre')

class AlterarGradeCurricularForm(forms.ModelForm):
    class Meta:
        model = GradeCurricular  
        fields = ('curso', 'ano','semestre')      

class GradeCurricularAdmin(admin.ModelAdmin):
    form = AlterarGradeCurricularForm
    add_form = NovoGradeCurricularForm

class GradeCurricularAdmin(UserAdmin):
    form = AlterarGradeCurricularForm
    add_form = NovoGradeCurricularForm
    list_display = ('curso', 'ano','semestre') 
    list_filter = ('curso', 'ano','semestre') 
    fieldsets = ( (None, {'fields': ('curso', 'ano','semestre') }),)
    add_fieldsets = (
        (None, {
            'fields': ('curso', 'ano','semestre') 

            } ),
             
         )
    search_fields = ('curso', 'ano','semestre') 
    ordering = ('ano',)
    filter_horizontal = ()    

# ----------------------------------------PERIODO    
class NovoPeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ('numero', 'curso', 'semestre','ano')

class AlterarPeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo  
        fields = ('numero', 'curso', 'semestre','ano')      

class PerriodoAdmin(admin.ModelAdmin):
    form = AlterarPeriodoForm
    add_form = NovoPeriodoForm 

class PeriodoAdmin(UserAdmin):
    form = AlterarPeriodoForm
    add_form = NovoPeriodoForm 
    list_display = ('numero', 'curso', 'semestre','ano')
    list_filter = ('numero', 'curso', 'semestre','ano')
    fieldsets = ( (None, {'fields': ('numero', 'curso', 'semestre','ano')}),)
    add_fieldsets = (
        (None, {
            'fields': ('numero', 'curso', 'semestre','ano')

            } ),
             
         )
    search_fields = ('numero', 'curso', 'semestre','ano')
    ordering = ('numero',)
    filter_horizontal = ()





#-------------------------------------------------------------------------------------------------#



class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo','carga_horaria')
    list_filter = ('tipo',)



admin.site.register(Aluno,                   AlunoAdmin)
admin.site.register(Professor,               ProfessorAdmin)

admin.site.register(Curso,                   CursoAdmin)

admin.site.register(Matricula                            )
admin.site.register(Disciplina                            )
admin.site.register(Periodo,                 PeriodoAdmin)
admin.site.register(GradeCurricular,         GradeCurricularAdmin)