from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from rest_framework import generics
from accounts.models import Company
from accounts.serializers import (
    CompanyCustomRegistrationSerializer, 
    EmployeeCustomRegistrationSerializer
    )

from django.core.mail import send_mail



class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyCustomRegistrationSerializer


class EmployeeRegistrationView(RegisterView):
    serializer_class = EmployeeCustomRegistrationSerializer