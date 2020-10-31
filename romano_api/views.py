from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from romano_api import serelizador
import math as m

class RomanoApiView(APIView):
    serializer_class= serelizador.RomanoSerializer
    def get(self, request, format=None):
        return Response({'message':"Bienvenido aqui podra cambiar numeros decimales a numeros romanos"})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        message=""
        if serializer.is_valid():
            numero=serializer.validated_data.get('numero')
            num=float(numero)
            values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
            letras = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
            i=0
            while num>0 and i<13:
                if num>=values[i]:
                    message+= str(letras[i])
                    num= num-values[i]
                else:
                    i+=1
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            