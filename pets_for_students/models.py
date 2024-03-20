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
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.ownerId.updateNoCats()  # Update the noCats attribute of the related Student instance.

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  # Call the "real" save() method.
        self.ownerId.updateNoCats()  # Update the noCats attribute of the related Student instance.

    def __str__(self):
        return self.name
