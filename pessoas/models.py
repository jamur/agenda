from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    institutions = models.ManyToManyField('Institution', related_name='people', through='role', blank=True)
    subjects = models.ManyToManyField('Subject', related_name='people', through='personsubject', blank=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=250)
    #people = models.ManyToManyField('Person', related_name='institutions')

    def __str__(self):
        return self.name

class Cargo(models.Model):
    nome_do_cargo = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_do_cargo

class Role(models.Model):
    role_name = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete = models.CASCADE, blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete = models.CASCADE, blank=True, null=True)

class Subject(models.Model):
    subject = models.CharField(max_length=200)
    #people = models.ManyToManyField('Person', related_name='subjects')

    def __str__(self):
        return self.subject


class PersonSubject(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)



# Create your models here.
