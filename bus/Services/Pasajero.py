from bus.models import Pasajeros
from bus.models import Lugar
from bus.models import Persona
from bus.models import ReservaPasajero
from bus.Serializers import PasajeroSerializer

class PasajeroService:    
    def __init__(self): 
        self.codigo = 0
        self.nombre = ''
        self.msg = ''
        self.data = ''
        self.resp = {}
    
    def get_pasajero(self, id):
        try:
            pasajero = Pasajeros.objects.filter(PRS_ID=id).first()
            if pasajero:
                data = PasajeroSerializer(pasajero)

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
            pasajeros = Pasajeros.objects.all()
            if pasajeros.count() > 0:
                data = PasajeroSerializer(pasajeros,many=True)
                
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
            nombre = data['nombre']
            apellido = data['apellido']
            rut = data['rut']
            n_reserva = data['nReserva']

            reserva_id = data['reservaId']
            reserva = ReservaPasajero.objects.get(RSV_ID=reserva_id)

            persona = Persona.objects.filter(PRS_VIGENCIA=1, PRS_RUT=rut).first()

            if persona:
                persona.PRS_VIGENCIA = 1
                persona.save()
            else:
                persona = Persona.objects.create(
                    PRS_NOMBRE = nombre,
                    PRS_APELLIDO = apellido,
                    PRS_RUT = rut
                )

            pasajero = Pasajeros.objects.create(
                PSR_N_RESERVA = n_reserva,
                PRS_ID = persona,
                VJE_ID = reserva,
            )

            self.codigo = 1
            self.msg = 'Pasajero creado correctamente'
            
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
            nombre = data['nombre']
            apellido = data['apellido']
            n_reserva = data['nReserva']
            pasajero_id = id

            pasajero = Pasajeros.objects.filter(PSR_ID=pasajero_id).first()
            persona = Persona.objects.filter(PRS_VIGENCIA=1, PRS_ID=pasajero.PRS_ID.PRS_ID).first()
            
            if persona:
                persona.PRS_NOMBRE = nombre
                persona.PRS_APELLIDO = apellido
                persona.save()

            if pasajero:
                pasajero.PSR_N_RESERVA = n_reserva
                pasajero.save()
                
                self.codigo = 1
                self.msg = 'Pasajero actualizado correctamente'
            else:
                self.msg = 'Pasajero no encontrado'

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
            pasajero = Pasajeros.objects.filter(PSR_VIGENCIA=1, PSR_ID=id).first()            

            if pasajero:
                pasajero.PSR_VIGENCIA = 0
                pasajero.save()

                self.codigo = 1
                self.msg = 'Pasajero deshabilitado correctamente'
            else:
                self.msg = 'Pasajero no encontrado'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp 
        