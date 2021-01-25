from django.conf.urls import include,url
from bus import views

urlpatterns = [
    url(r'^bus/$', views.bus, name='bus_all_add'),
    url(r'^bus/(?P<id>\w+)/$', views.bus, name='bus_update_del'),
    url(r'^chofer/$', views.chofer, name='chofer_all_add'),
    url(r'^chofer/(?P<id>\w+)/$', views.chofer, name='chofer_update_del'),
    url(r'^trayecto/$', views.trayecto, name='trayecto_all_add'),
    url(r'^trayecto/(?P<id>\w+)/$', views.trayecto, name='trayecto_update_del'),
    url(r'^reserva/$', views.reserva, name='reserva_all_add'),
    url(r'^reserva/(?P<id>\w+)/$', views.reserva, name='reserva_update_del'),
    url(r'^reserva/(?P<id>\w+)/pasajero/$', views.reserva_pasajero, name='reserva_pasajero'),
    url(r'^pasajero/$', views.pasajero, name='pasajero_all_add'),
    url(r'^pasajero/(?P<id>\w+)/$', views.pasajero, name='pasajero_update_del'),
    url(r'^lugares/$', views.lugares, name='lugares_all'),
    url(r'^estados/$', views.estados, name='estados_all'),
    url(r'^trayecto/(?P<id>\w+)/buses/$', views.trayecto_buses, name='trayecto_buses'),
]