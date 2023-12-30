from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


# Create your views here.

def home(request):
    return render(request, 'index.html', {})


class MenuViewSet(viewsets.ViewSet):
    def list(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        menu_item = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(menu_item)
        return Response(serializer.data)


# class SingleMenuViewSet(viewsets.ViewSet):
#     def retrieve(self, request, pk=None):
#         menu_item = Menu.objects.get(pk=pk)
#         serializer = MenuSerializer(menu_item)
#         return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
