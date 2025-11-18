from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_image = models.FileField(upload_to='projects/')
    project_description = models.TextField()

    def __str__(self):
        return self.project_name



class Client(models.Model):
    client_image = models.FileField(upload_to='clients/')
    client_name = models.CharField(max_length=200)
    client_designation = models.CharField(max_length=200)
    client_description = models.TextField()

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
