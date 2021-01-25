from django.contrib import admin

# Register your models here.
from bus.models import *

admin.site.register(Bus)
admin.site.register(Chofer)
admin.site.register(Estado)
admin.site.register(Lugar)
admin.site.register(Pasajeros)
admin.site.register(Persona)
admin.site.register(ReservaPasajero)
admin.site.register(Trayecto)

