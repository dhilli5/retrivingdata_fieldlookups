from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.course_name
class Student(models.Model):
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    st_name=models.CharField(max_length=100,unique=True)
    mno=models.IntegerField()
    
    def __str__(self):
        return self.st_name
    
class Address(models.Model):
    st_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
    