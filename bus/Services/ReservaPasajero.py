from bus.models import ReservaPasajero
from bus.models import Trayecto
from bus.models import Bus
from bus.models import Chofer
from bus.models import Estado
from bus.models import Lugar
from bus.models import Pasajeros
from bus.Serializers import ReservaPasajeroSerializer
from bus.Serializers import PasajeroSerializer

class ReservaService:    
    def __init__(self): 
        self.codigo = 0
        self.nombre = ''
        self.msg = ''
        self.data = ''
        self.resp = {}

    def get_reserva(self, id):
        try:
            reserva = ReservaPasajero.objects.filter(RSV_ID=id).first()
            if reserva:
                data = ReservaPasajeroSerializer(reserva)

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
            reservas = ReservaPasajero.objects.all()
            if reservas.count() > 0:
                data = ReservaPasajeroSerializer(reservas,many=True)
                
                i=0
                for dato in data.data:
                    """ Se ingresa el nombre del origen y destino """
                    lugar_inicio = Lugar.objects.get(LGR_ID=dato['TYO_ID']['LGR_ID_INICIO'])
                    data.data[i]['TYO_ID']['nombre_origen'] = lugar_inicio.LGR_NOMBRE
                    lugar_destino = Lugar.objects.get(LGR_ID=dato['TYO_ID']['LGR_ID_TERMINO'])
                    data.data[i]['TYO_ID']['nombre_destino'] = lugar_destino.LGR_NOMBRE
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
            #TODO: DESPUÉS VALIDAR FECHA, UBICACIÓN, ENTRE OTROS, ETC.
            trayecto_id = data['trayectoId']
            fecha_inicio = data['fechaInicio']
            fecha_llegada = data['fechaLlegada']

            bus_id = data['busId']
            chofer_id = data['choferId']

            trayecto = Trayecto.objects.get(TYO_ID = trayecto_id)
            bus = Bus.objects.get(BUS_ID = bus_id)
            chofer = Chofer.objects.get(CFR_ID = chofer_id)
            estado = Estado.objects.get(EST_ID = 1)

            reserva = ReservaPasajero.objects.create(
                TYO_ID = trayecto,
                FDT_DIA_INICIO=fecha_inicio,
                FDT_DIA_LLEGADA=fecha_llegada,
                BUS_ID=bus,
                CFR_ID=chofer,
                EST_ID=estado
            )

            self.codigo = 1
            self.msg = 'Reserva creada correctamente'
            
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
            trayecto_id = data['trayectoId']
            fecha_inicio = data['fechaInicio']            
            fecha_llegada = data['fechaLlegada']
            bus_id = data['busId']
            chofer_id = data['choferId']
            estado = data['estado']
            vigencia = data['vigencia']

            trayecto = Trayecto.objects.get(TYO_ID = trayecto_id)
            bus = Bus.objects.get(BUS_ID = bus_id)
            chofer = Chofer.objects.get(CFR_ID = chofer_id)
            estado = Estado.objects.get(EST_ID = estado)

            reserva = ReservaPasajero.objects.filter(RSV_ID=id).first()

            if reserva:
                reserva.TYO_ID=trayecto
                reserva.FDT_DIA_INICIO=fecha_inicio
                reserva.FDT_DIA_LLEGADA=fecha_llegada
                reserva.BUS_ID=bus
                reserva.CFR_ID=chofer
                reserva.EST_ID=estado
                reserva.RSV_VIGENCIA=vigencia
                
                reserva.save()

                self.codigo = 1
                self.msg = 'Reserva actualizada correctamente'
            else:
                self.msg = 'Reserva no encontrada'

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
            reserva = ReservaPasajero.objects.filter(RSV_ID=id).first()

            if reserva:
                reserva.RSV_VIGENCIA = 0
                reserva.save()

                self.codigo = 1
                self.msg = 'Reserva deshabilitado correctamente'
            else:
                self.msg = 'Reserva no encontrado'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp

    def get_reserva_pasajero(self, id):
        """ Obtiene los pasajeros de una reserva(programa) """
        try:
            reserva = ReservaPasajero.objects.get(RSV_ID=id)            
            pasajero = Pasajeros.objects.filter(VJE_ID=reserva, PSR_VIGENCIA=1).all()
            if pasajero.count() > 0:
                data = PasajeroSerializer(pasajero,many=True)

                self.data = data.data
                self.codigo = 1
                self.msg = 'Data desplegada.'
            else:
                self.msg = 'Sin data.'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp

        