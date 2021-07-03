from django.db import models

# Create your models here.
class Courses(models.Model):
    courseName=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics')
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.courseName

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return "{} - {}".format(self.name,self.email)


class Faculty(models.Model):
    facultyName=models.CharField(max_length=50)
    profession=models.CharField(max_length=50)
    image=models.ImageField(upload_to='faculty')
    instagram=models.URLField(max_length=300,default='http://google.com')
    github=models.URLField(max_length=300,default='http://google.com')
    linkedin=models.URLField(max_length=300,default='http://google.com')

    def __str__(self):
        return "{} - {}".format(self.facultyName,self.profession)

class Payment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    nameoncard=models.CharField(max_length=50)
    creditcardnumber=models.CharField(max_length=50)
    date=models.DateField()
    cvv=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    courseName=models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} - {}".format(self.name,self.email,self.courseName)
