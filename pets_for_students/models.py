from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    noCats = models.IntegerField(default=0)

    def updateNoCats(self):
        self.noCats = self.cat_set.count()
        self.save()
        return self.cat_set.count()

    def __str__(self):
        return self.firstName + " " + self.lastName
    
class Cat(models.Model):
    name = models.CharField(max_length=64)
    ownerId = models.ForeignKey(Student, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.ownerId.updateNoCats()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.ownerId.updateNoCats()

    def __str__(self):
        return self.name
