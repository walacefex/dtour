from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )

    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )

    genero = models.CharField(
        max_length=255,
        verbose_name='Gênero',
        choices=GENEROS
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    password = models.CharField(
        max_length=225,
        verbose_name='password'
    )

    biografia = models.TextField(
        null=True,
        blank=True
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Ideia(models.Model):
    CATEGORIAS = (
        ('TERRA_PLANA', 'Terra Plana'),
        ('CONTRA_GROGER', 'Ideias para Coach Groger'),
        ('CONTRA_JOAO', 'Ideias contra João'),
        ('PUBLICAS', 'Públicas'),
        ('OUTROS', 'Outros'),
    )

    pessoa = models.ForeignKey(
        Pessoa, on_delete=None
    )

    titulo = models.CharField(
        max_length=255, 
        verbose_name='Nome de ideia',
        unique=True)

    descricao = models.TextField(
        verbose_name='Descreva sua ideia'
    )

    categorias = models.CharField(
        verbose_name='Categorias',
        choices=CATEGORIAS,
        max_length=255
    )

    categoria_outros = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Caso outros, qual?'
    )
    
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.pessoa.nome + ' - ' + self.categorias

