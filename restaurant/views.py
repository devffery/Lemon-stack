# views.py
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

# Handles GET (list) and POST (create)
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve), PUT (update), and DELETE (destroy)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
