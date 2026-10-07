from django.shortcuts import render

from django.contrib.auth.models import User 

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import authentication,permissions

from staff.models import  Doctor

from staff_v2.serializers import DoctorSerializers,UserSerializers


# Create your views here.

class DoctorListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request):

        qs = Doctor.objects.all()  #qs =>  PYNT
        
        serializer_instance = DoctorSerializers(qs,many=True)
        
        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data  # PYNT => qs

        serializer_instance = DoctorSerializers(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Doctor.objects.create(**cleaned_data)

            return Response (data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)


class DoctorRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    
    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs = Doctor.objects.get(id=pk)

        serializer_instance=DoctorSerializers(qs)

        return Response (data=serializer_instance.data) 

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instance = DoctorSerializers(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance._validated_data

            Doctor.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        qs = Doctor.objects.filter(id=pk).delete()

        return Response (data={"message":"record deleted"})


class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializers(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

        







 



        

        







    

    



    
    
