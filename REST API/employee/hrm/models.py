from django.db import models

# Create your models here.
class Users(models.Model):
    employee_id = models.CharField(max_length = 10 ,unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField()

    def upload_photo(self,filename):
        path = 'hrm/photo/{}'.format(filename)
        return path
    photo = models.ImageField(upload_to=upload_photo,blank=True, null=True)

    def upload_file(self,filename):
        path = 'hrm/file/{}'.format(filename)
        return path
    photo = models.ImageField(upload_to=upload_file, blank=True, null=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"