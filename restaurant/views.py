# views.py
from rest_framework import generics, viewsets
from .models import Menu , Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
   

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve), PUT (update), and DELETE (destroy)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
