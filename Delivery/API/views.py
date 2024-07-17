from django.shortcuts import render
from .serializers import DeliverySerializer
from .models import Delivery
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['GET','POST'])
def deliveries(request):
    if request.method == 'GET':
        deliver = Delivery.objects.all()
        serializer = DeliverySerializer(deliver,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['PUT','GET'])       
def update_delivery(request,pk):
    if request.method == 'PUT':
        deliver = get_object_or_404(Delivery,id=pk)
        serializer = DeliverySerializer(deliver,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'GET': 
        deliver = get_object_or_404(Delivery,id=pk)
        serializer = DeliverySerializer(deliver)
        return Response(serializer.data)
