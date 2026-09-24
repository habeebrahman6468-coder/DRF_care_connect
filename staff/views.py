from django.shortcuts import render


from staff.models import Doctor

from rest_framework.views import APIView

from rest_framework.response import Response
# Create your views here.

from rest_framework import serializers

class DoctorListCreateView(APIView):


    def get(self,request):

        qs = Doctor.objects.all().values()

        doctors_list = list(qs)

        return Response(data=doctors_list)

    def post(self,request):

        #form_data = json.loads(request.body)X

        form_data = request.data

        specialization = form_data.get("specialization")

        flat = [tp[0] for tp in Doctor.SPECIALIZATION_OPTIONS]

        if specialization not in flat:

            raise serializers.ValidationError(specialization+ "is not a valid choice")

        fee = form_data.get("fee")

        if fee > 1500:

            raise serializers.ValidationError("invalid fee , fee should be < 1500")


        Doctor.objects.create(**form_data)

        return Response(data={"message":"created"})




class DoctorRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs = Doctor.objects.filter(id=pk).values()

        docter_list = list(qs)

        return Response(data=docter_list)

    def put(self,request,pk=None):

        form_data = request.data

        Doctor.objects.filter(id=pk).upadte(**form_data)

        return Response(data={"message":"updated..."})

    def delete(self,request,pk=None):

        Doctor.objects.get(id=pk).delete()

        return Response(data={"message":"deleted...."})