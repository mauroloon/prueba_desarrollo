from django.db import models

class Persona(models.Model):
    PRS_ID = models.AutoField(primary_key=True)
    PRS_NOMBRE = models.CharField(max_length=100,blank=True, null=True)
    PRS_APELLIDO = models.CharField(max_length=100,blank=True, null=True)
    PRS_RUT = models.CharField(max_length=100,blank=False, null=False)
    PRS_VIGENCIA = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = 'Personas'
        ordering = ['PRS_ID']

    def __str__(self):
        return self.PRS_NOMBRE + ' ' + self.PRS_APELLIDO