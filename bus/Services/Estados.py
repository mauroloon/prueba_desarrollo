from bus.models import Estado
from bus.Serializers import EstadoSerializer

class EstadosService:    
    def __init__(self): 
        self.codigo = 0
        self.nombre = ''
        self.msg = ''
        self.data = ''
        self.resp = {}

    def get_all(self):
        try:
            estados = Estado.objects.all()
            print(estados)
            if estados.count() > 0:
                data = EstadoSerializer(estados,many=True)
                
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
