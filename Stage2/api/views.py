# from django.shortcuts import render
from .models import person
from rest_framework import generics
from .serializers import pSerializer


class list_person(generics.ListAPIView):
    queryset = person.objects.all()
    serializer_class = pSerializer
class C_person(generics.CreateAPIView):
    queryset = person.objects.all()
    serializer_class = pSerializer


class R_person(generics.RetrieveAPIView):
    queryset = person.objects.all()
    serializer_class = pSerializer
    lookup_field = 'id'


class U_person(generics.UpdateAPIView):
    queryset = person.objects.all()
    serializer_class = pSerializer
    lookup_field = 'id'


class D_person(generics.DestroyAPIView):
    queryset = person.objects.all()
    serializer_class = pSerializer
    lookup_field = 'id'