from django.urls import path

from booking_v2.views import SignupView
from booking_v2.views import AppointmentListCreateView,AppointmentRetrieveUpdateDeleteView

urlpatterns=[

    path('signup/',SignupView.as_view()),
    path('appointments/',AppointmentListCreateView.as_view()),
    path('appointments/<int:pk>/',AppointmentRetrieveUpdateDeleteView.as_view()),
 
]