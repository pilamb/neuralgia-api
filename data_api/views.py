from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from data_api.models import Hit
from data_api.serializers import HitSerializer

@api_view(['GET', 'POST'])
def hits_list(request, format=None):
    """
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        hits = Hit.objects.all()
        serializer = HitSerializer(hits, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def hit_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code Hit.
    """
    try:
        hit = Hit.objects.get(pk=pk)
    except Hit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HitSerializer(hit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HitSerializer(hit, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
