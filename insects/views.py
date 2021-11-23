from rest_framework import generics
from .models import Insect
from .serializer import InsectSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


class InsectListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Insect.objects.all()
    serializer_class = InsectSerializer


class InsectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Insect.objects.all()
    serializer_class = InsectSerializer