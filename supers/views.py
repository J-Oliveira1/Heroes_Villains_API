from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Superserializer
from .models import Super

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = Superserializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = Superserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = Superserializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Superserializer(super, data=request.data, status=status.HTTP_200_OK)
        serializer.save()
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

