from django.shortcuts import render
import random
# Create your views here.
from rest_framework import serializers
from .models import Product,User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self,request,id=None):
        if id is None:
            data=Product.objects.all()
            serializer=ProductSerializer(data,many=True)
        else:
            print("id is true")
            data=Product.objects.get(id=id)
            serializer=ProductSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        datas=request.data
        serializer=ProductSerializer(data=datas)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


    def put(self,request,id):
        datas=Product.objects.get(id=id)
        serializer=ProductSerializer(datas,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    def patch(self,request,id):
        datas=Product.objects.get(id=id)
        serializer=ProductSerializer(datas,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"partially upate"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        

    def delete(self,request,id):
        datas=Product.objects.get(id=id)
        datas.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)



class UserView(APIView):
    def get(self,request):
        users=User.objects.all()
        user=random.choice(users)
        return Response({'user':user.id})
    