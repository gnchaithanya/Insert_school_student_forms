from django.db import models

# Create your models here.
class School(models.Model):
    ScName=models.CharField(max_length=100,primary_key=True)
    ScPrincipal=models.CharField(max_length=100)
    ScLocation=models.CharField(max_length=100)

    def __str__(self):
        return self.ScName
    
class Student(models.Model):
    ScName=models.ForeignKey(School,on_delete=models.CASCADE)
    Sname=models.CharField(max_length=100)
    Sid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.Sname