# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


#from django.contrib.auth.models import User
class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    ra = models.IntegerField(unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default='C')
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    @property   #Objetos para roubar
    def is_staff(self):
        return self.perfil == 'C'  


    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True


    def get_short_name(self):
        return self.nome
    def get_full_name(self):
        return self.nome

    def __str__(self):
        return self.nome


class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(unique=True, max_length=50)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default = True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome 

class Aluno(Usuario):
    celular = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso)

class Professor(Usuario):
    apelido = models.CharField(max_length=30,unique = True, null = True)
    curso = models.ForeignKey(Curso)

class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', db_column='curso', null=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    USERNAME_FIELD = 'ano'


class Periodo(models.Model):
    curso = models.ForeignKey(to='GradeCurricular', db_column="curso", null=False, blank=False) #onetomany
    ano = models.ForeignKey(to='GradeCurricular', db_column="ano", null=False, related_name="ano_grade")
    semestre = models.ForeignKey(to='GradeCurricular', db_column="semestre", null=False,related_name="semestre_grade")
    numero = models.SmallIntegerField(null=False) #tinyint

    USERNAME_FIELD = 'numero'


class Disciplina(models.Model):
    nome = models.CharField(max_length=240,primary_key=True)
    carga_horaria = models.SmallIntegerField()  #tinyint
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()   



class Matricula(models.Model):
    nome = models.CharField(primary_key=True, max_length=50)
    sobrenome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    numero = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
'''
class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', related_name="gradesCurriculares", null=False, blank=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    def __str__(self):
        return self.nome     

class Periodo(models.Model):
    GradeCurricular = models.ForeignKey(to='GradeCurricular', related_name="periodos", null=False, blank=False) #onetomany
    numero = models.SmallIntegerField(null=False) #tinyint
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return self.nome  

'''










        


