from bus.models import Trayecto
from bus.models import Lugar
from bus.models import ReservaPasajero
from bus.models import Pasajeros
from bus.models import Bus
from bus.Serializers import TrayectoSerializer

class TrayectoService:    
    def __init__(self): 
        self.codigo = 0
        self.nombre = ''
        self.msg = ''
        self.data = ''
        self.resp = {}

    def get_trayecto(self, id):
        try:
            trayecto = Trayecto.objects.filter(TYO_ID=id).first()
            if trayecto:
                data = TrayectoSerializer(trayecto)
                
                self.data = data.data
                self.codigo = 1            
                self.msg = 'Data desplegada'
            else:
                self.msg = 'Sin data'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp
    
    def get_all(self):
        
        try:
            trayectos = Trayecto.objects.all()
            if trayectos.count() > 0:
                data = TrayectoSerializer(trayectos,many=True)

                i=0
                for dato in data.data:
                    """ Se colocal el nombre de origen y destino """
                    lugar_inicio = Lugar.objects.get(LGR_ID=dato['LGR_ID_INICIO'])
                    data.data[i]['nombre_origen'] = lugar_inicio.LGR_NOMBRE
                    lugar_destino = Lugar.objects.get(LGR_ID=dato['LGR_ID_TERMINO'])
                    data.data[i]['nombre_destino'] = lugar_destino.LGR_NOMBRE
                    """ Promedio de pasajeros por trayecto """
                    totalPasajeros = Pasajeros.objects.filter(PSR_VIGENCIA=1, VJE_ID__TYO_ID=dato['TYO_ID']).count()
                    totalReservasTrayecto = ReservaPasajero.objects.filter(TYO_ID=dato['TYO_ID']).count()
                    if totalPasajeros == 0 and totalReservasTrayecto == 0:
                        data.data[i]['promedio'] = 0
                    else:
                        data.data[i]['promedio'] = totalPasajeros/totalReservasTrayecto
                    i=i+1
                
                self.data = data.data
                self.codigo = 1            
                self.msg = 'Data desplegada'
            else:
                self.msg = 'Sin data'
            
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp

    def add(self, data):
        try:
            lugar_inicio_id = data['lugarInicioId']
            lugar_termino_id = data['lugarTerminoId']
            
            lugar_inicio = Lugar.objects.get(LGR_ID=lugar_inicio_id)
            lugar_termino = Lugar.objects.get(LGR_ID=lugar_termino_id)

            trayecto = Trayecto.objects.create(
                LGR_ID_INICIO = lugar_inicio.LGR_ID,
                LGR_ID_TERMINO = lugar_termino.LGR_ID
            )
            
            self.codigo = 1
            self.msg = 'Trayecto creado correctamente'
            
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp

    def update(self, data, id):
        try:
            lugar_inicio_id = data['lugarInicioId']
            lugar_termino_id = data['lugarTerminoId']
            vigencia = data['vigencia']
            
            lugar_inicio = Lugar.objects.get(LGR_ID=lugar_inicio_id)
            lugar_termino = Lugar.objects.get(LGR_ID=lugar_termino_id)

            trayecto = Trayecto.objects.filter(TYO_ID = id).first()

            if trayecto:
                trayecto.LGR_ID_INICIO = lugar_inicio.LGR_ID
                trayecto.LGR_ID_TERMINO = lugar_termino.LGR_ID
                trayecto.TYO_VIGENCIA = vigencia

                trayecto.save()

                self.codigo = 1
                self.msg = 'Trayecto actualizado correctamente'
            else:
                self.msg = 'Trayecto no encontrado'

        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp
    
    def delete(self, id):
        try:            
            trayecto = Trayecto.objects.filter(TYO_ID = id).first()

            if trayecto:
                trayecto.TYO_VIGENCIA = 0
                trayecto.save()

                self.codigo = 1
                self.msg = 'Trayecto deshabilitado correctamente'
            else:
                self.msg = 'Trayecto no encontrado'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp
    
    def get_buses_trayecto(self, id):
        #Filtrar a todos los buses de un trayecto con más del N % de su capacidad vendida.
        try:
            buses = ReservaPasajero.objects.filter(TYO_ID=id).values('BUS_ID','RSV_ID')
            
            reservas = []
            if len(buses) > 0:
                for bus in buses:
                    totalPasajeros = Pasajeros.objects.filter(PSR_VIGENCIA=1, VJE_ID=bus['RSV_ID']).count()
                    busObjecto = Bus.objects.get(BUS_ID=bus['BUS_ID'])
                    
                    data = {
                        'reserva': bus['RSV_ID'],
                        'bus': f'{busObjecto.BUS_MARCA} {busObjecto.BUS_MODELO}',
                        'porcentaje': (totalPasajeros * 100) / 20
                    }
                    
                    reservas.append(data)
                
                self.msg = 'Data desplegada'
                self.codigo=1
                self.data=reservas
            else:
                self.msg = 'Sin data'
            
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp
    

        