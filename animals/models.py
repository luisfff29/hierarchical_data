from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    pass


class Animals(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class MPPTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
