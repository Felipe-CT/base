from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    alias = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    birthday = models.TextField(default='')
    pks= models.ManyToManyField('Usuario', related_name="pokers")
    history= models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Poke(models.Model):

    created_at=models.DateTimeField(auto_now_add=True)
    creator= models.ForeignKey(Usuario, related_name="pokes_given", on_delete=models.CASCADE)
    receiver= models.ForeignKey(Usuario, related_name="pokes_received", on_delete=models.CASCADE)




