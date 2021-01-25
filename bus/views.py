from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from bus.Services import BusService
from bus.Services import ChoferService
from bus.Services import TrayectoService
from bus.Services import ReservaService
from bus.Services import PasajeroService
from bus.Services import EstadosService


@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([AllowAny,])
def bus(request,id=None):
    service = BusService()
    if request.method == 'GET':
        if id:
            response = service.get_bus(id)
        else:
            response = service.get_all()
    if request.method == 'POST':
        data_param = request.POST.dict()
        response = service.add(data_param)
    if request.method == 'PUT':
        data_param = request.POST.dict()
        response = service.update(data_param, id)
    if request.method == 'DELETE':
        response = service.delete(id)
    return Response(response)

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([AllowAny,])
def chofer(request,id=None):
    service = ChoferService()
    if request.method == 'GET':
        if id:
            response = service.get_chofer(id)
        else:
            response = service.get_all()
    if request.method == 'POST':
        data_param = request.POST.dict()
        response = service.add(data_param)
    if request.method == 'PUT':
        data_param = request.POST.dict()
        response = service.update(data_param, id)
    if request.method == 'DELETE':
        response = service.delete(id)
    return Response(response)

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([AllowAny,])
def trayecto(request,id=None):
    service = TrayectoService()
    if request.method == 'GET':
        if id:
            response = service.get_trayecto(id)
        else:
            response = service.get_all()
    if request.method == 'POST':
        data_param = request.POST.dict()
        response = service.add(data_param)
    if request.method == 'PUT':
        data_param = request.POST.dict()
        response = service.update(data_param, id)
    if request.method == 'DELETE':
        response = service.delete(id)
    return Response(response)

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([AllowAny,])
def reserva(request,id=None):
    service = ReservaService()
    if request.method == 'GET':
        if id:
            response = service.get_reserva(id)
        else:            
            response = service.get_all()
    if request.method == 'POST':
        data_param = request.POST.dict()
        response = service.add(data_param)
    if request.method == 'PUT':
        data_param = request.POST.dict()
        response = service.update(data_param, id)
    if request.method == 'DELETE':
        response = service.delete(id)
    return Response(response)

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([AllowAny,])
def pasajero(request,id=None):
    service = PasajeroService()
    if request.method == 'GET':
        if id:
            response = service.get_pasajero(id)
        else:
            response = service.get_all()
    if request.method == 'POST':
        data_param = request.POST.dict()
        response = service.add(data_param)
    if request.method == 'PUT':
        data_param = request.POST.dict()
        response = service.update(data_param, id)
    if request.method == 'DELETE':
        response = service.delete(id)
    return Response(response)

@api_view(['GET'])
@permission_classes([AllowAny,])
def lugares(request,id=None):
    service = BusService()
    if request.method == 'GET':
        response = service.get_all_lugares()
    return Response(response)

@api_view(['GET'])
@permission_classes([AllowAny,])
def estados(request,id=None):
    service = EstadosService()
    if request.method == 'GET':
        response = service.get_all()
    return Response(response)

@api_view(['GET'])
@permission_classes([AllowAny,])
def reserva_pasajero(request,id=None):
    service = ReservaService()
    if request.method == 'GET':
        response = service.get_reserva_pasajero(id)
    return Response(response)


@api_view(['GET'])
@permission_classes([AllowAny,])
def trayecto_buses(request,id=None):
    service = TrayectoService()
    if request.method == 'GET':
        response = service.get_buses_trayecto(id)
    return Response(response)