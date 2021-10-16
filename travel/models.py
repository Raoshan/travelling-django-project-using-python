from django.db import models

# 1.
# class Destination():
#     id : int
#     name : str
#     img : str
#     desc : str
#     price : int
#     offer : bool

# 2.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
