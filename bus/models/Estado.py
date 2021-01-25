from django.db import models

class Estado(models.Model):
    EST_ID = models.AutoField(primary_key=True)
    EST_NOMBRE = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = 'Estados'
        ordering = ['EST_ID']

    def __str__(self):
        return self.EST_NOMBRE