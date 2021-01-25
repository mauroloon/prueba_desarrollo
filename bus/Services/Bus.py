from bus.models import Bus
from bus.models import Lugar
from bus.Serializers import BusSerializer
from bus.Serializers import LugarSerializer

class BusService:    
    def __init__(self): 
        self.codigo = 0
        self.nombre = ''
        self.msg = ''
        self.data = ''
        self.resp = {}

    def get_bus(self, id):
        try:
            bus = Bus.objects.filter(BUS_ID = id).first()
            if bus:
                data = BusSerializer(bus)
                
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
            buses = Bus.objects.all()
            if buses.count() > 0:
                data = BusSerializer(buses,many=True)
                
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
            marca = data['marca']
            modelo = data['modelo']

            lugar = Lugar.objects.get(LGR_ID=lugar_id)

            bus = Bus.objects.create(
                BUS_MARCA = marca,
                BUS_MODELO = modelo,
                LGR_ID = lugar
            )
            
            self.codigo = 1
            self.msg = 'Bus creado correctamente'
            
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
            marca = data['marca']
            modelo = data['modelo']
            vigencia = data['vigencia']

            lugar = Lugar.objects.get(LGR_ID=lugar_id)
            bus = Bus.objects.filter(BUS_ID = id).first()

            if bus:
                bus.BUS_MARCA = marca
                bus.BUS_MODELO = modelo
                bus.LGR_ID = lugar
                bus.BUS_VIGENCIA = vigencia

                bus.save()

                self.codigo = 1
                self.msg = 'Bus actualizado correctamente'
            else:
                self.msg = 'Bus no encontrado'

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
        """ Deshabilitar bus """
        try:            
            bus = Bus.objects.filter(BUS_ID = id).first()

            if bus:
                bus.BUS_VIGENCIA = 0
                bus.save()

                self.codigo = 1
                self.msg = 'Bus deshabilitado correctamente'
            else:
                self.msg = 'Bus no encontrado'
        except Exception as e:
            self.nombre = 'Error'
            self.msg = e
        finally:
            self.resp["code"] = self.codigo
            self.resp["name"] = self.nombre
            self.resp["message"] = self.msg
            self.resp["data"] = self.data
        return self.resp
    
    def get_all_lugares(self):
        try:
            lugares = Lugar.objects.all()
            if lugares.count() > 0:
                data = LugarSerializer(lugares,many=True)
                
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
        