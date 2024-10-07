from django.db import models

# Create your models here.

class RoomModel(models.Model):
    code = models.CharField(max_length=10,verbose_name='کد ملی')
    