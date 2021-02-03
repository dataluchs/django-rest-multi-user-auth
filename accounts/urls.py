from django.urls import path
from accounts.views import CompanyRegistrationView, EmployeeRegistrationView

app_name = 'accounts'

urlpatterns = [
    #Registration Urls
    path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
    path('registration/employee/', EmployeeRegistrationView.as_view(), name='register-employee'),
]