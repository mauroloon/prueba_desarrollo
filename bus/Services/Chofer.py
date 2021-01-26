from bus.models import Chofer
from bus.models import Lugar
from bus.Serializers import ChoferSerializer

class ChoferService:    
    def __init__(self): 
        self.codigo = 0
        self.nombre = ''
        self.msg = ''
        self.data = ''
        self.resp = {}

    def get_chofer(self,id):
        try:
            chofer = Chofer.objects.filter(CFR_ID=id).first()
            if chofer:
                data = ChoferSerializer(chofer)
                
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
            choferes = Chofer.objects.all()
            if choferes.count() > 0:
                data = ChoferSerializer(choferes,many=True)
                
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
            lugar_id = data['lugarId']
            nombre = data['nombre']
            apellido = data['apellido']
            rut = data['rut']
            
            lugar = Lugar.objects.get(LGR_ID=lugar_id)

            chofer = Chofer.objects.create(
                CFR_NOMBRE = nombre,
                CFR_APELLIDO = apellido,
                CFR_RUT = rut,
                LGR_ID = lugar
            )
            
            self.codigo = 1
            self.msg = 'Chofer creado correctamente'
            
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
            lugar_id = data['lugarId']
            nombre = data['nombre']
            apellido = data['apellido']
            rut = data['rut']
            vigencia = data['vigencia']

            lugar = Lugar.objects.get(LGR_ID=lugar_id)
            chofer = Chofer.objects.filter(CFR_ID = id).first()

            if chofer:
                chofer.CFR_NOMBRE = nombre
                chofer.CFR_APELLIDO = apellido
                chofer.CFR_RUT = rut
                chofer.LGR_ID = lugar
                chofer.CFR_VIGENCIA = vigencia

                chofer.save()

                self.codigo = 1
                self.msg = 'Chofer actualizado correctamente'
            else:
                self.msg = 'Chofer no encontrado'

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
            chofer = Chofer.objects.filter(CFR_ID = id).first()

            if chofer:
                chofer.CFR_VIGENCIA = 0
                chofer.save()

                self.codigo = 1
                self.msg = 'Chofer deshabilitado correctamente'
            else:
                self.msg = 'chofer no encontrado'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp
        