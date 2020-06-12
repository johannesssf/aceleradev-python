from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último acesso', auto_now_add=True)
    email = models.EmailField('Email')
    password = models.CharField(
        'Senha',
        max_length=50,
        validators=[MinLengthValidator(8)]
    )

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Versão', max_length=5)
    address = models.GenericIPAddressField('Endereço', max_length=39)

    def __str__(self):
        return self.name


class Event(models.Model):
    LEVELS = (
        ('critical', 'CRITICAL'),
        ('debug', 'DEBUG'),
        ('error', 'ERROR'),
        ('warning', 'WARNING'),
        ('info', 'INFO'),
    )
    level = models.CharField('Nível', max_length=20, choices=LEVELS)
    data = models.TextField('Dados')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Data', auto_now_add=True)
    agent = models.ForeignKey('Agent', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.level


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
