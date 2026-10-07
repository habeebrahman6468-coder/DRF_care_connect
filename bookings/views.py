from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Appointment
from bookings.serializer import AppointmentSerializer

from staff.models import Doctor

# Create your views here.


class AppointmentListCreateView(APIView):

    def get(self,request):

        qs = Appointment.objects.all()

        serializer_instance = AppointmentSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = AppointmentSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            doctor = cleaned_data.get('doctor')

            appointment_date = cleaned_data.get('appointment_date') 

            last_appointment_object = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()

            if last_appointment_object:

                new_token = appointment_date.token_number+1

            else: new_token=1

            doctor_object = Doctor.objects.get(id=doctor)

            cleaned_data["doctor"]=doctor_object        #=> ["doctor"] currently an integer

            Appointment.objects.create(**cleaned_data,token_number = new_token)

            response_data = {    
               "status":"booked",
               "token":new_token

            }

            return Response(data=response_data)

        else:
            return Response(data=serializer_instance.errors)  


class AppointmentRetrieveUpdateDelete(APIView):

#     def get(self,request,pk=None):

#         qs =Appointment.objects.get(id=pk)                

#         serializer_instance = AppointmentSerializer(qs)

#         return Response(data=serializer_instance.data)


    def get(self, request, pk=None):

        qs = Appointment.objects.get(id=pk)

        doctor_object = qs.doctor

        response_data = {
            "patient_name": qs.patient_name,
            "phone": qs.phone,
            "doctor": doctor_object.id,
            "appointment_date": qs.appointment_date,
            "token_number": qs.token_number,
            "appointment_time": qs.appointment_time,
            "problem": qs.problem,
            "created_at": qs.created_at
        }

        return Response(data=response_data)


    def put(self,request,pk=None):
    
            form_data = request.data
    
            serializer_instance = AppointmentSerializer(data=form_data)
    
            if serializer_instance.is_valid():
    
                cleaned_data = serializer_instance._validated_data
    
                Appointment.objects.filter(id=pk).update(**cleaned_data)
    
                return Response(data=serializer_instance.validated_data)
    
            else:
    
                return Response(data=serializer_instance.errors)
    
    def delete(self,request,pk=None):
    
        Appointment.objects.filter(id=pk).delete()
    
        return Response (data={"message":"record deleted"})
    
    
  
    
            
    
    


            
             