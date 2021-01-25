from django.db import models

class Lugar(models.Model):
    LGR_ID = models.AutoField(primary_key=True)
    LGR_NOMBRE = models.CharField(max_length=100, blank=False, null=False)
    LGR_DESCRIPCION = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = 'Lugares'
        ordering = ['LGR_ID']

    def __str__(self):
        return self.LGR_NOMBRE