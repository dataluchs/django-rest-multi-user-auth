from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from accounts.models import Company, Employee


class CompanyCustomRegistrationSerializer(RegisterSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    industry = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(CompanyCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'industry' : self.validated_data.get('industry', ''),
                'address' : self.validated_data.get('address', ''),
                'description': self.validated_data.get('description', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(CompanyCustomRegistrationSerializer, self).save(request)
        user.is_company = True
        user.save()
        company = Company(company=user, industry=self.cleaned_data.get('industry'), 
                address=self.cleaned_data.get('address'),
                description=self.cleaned_data.get('description'))
        company.save()
        return user


class EmployeeCustomRegistrationSerializer(RegisterSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    job_title = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(EmployeeCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'job_title' : self.validated_data.get('job_title', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(EmployeeCustomRegistrationSerializer, self).save(request)
        user.is_employee = True
        user.save()
        employee = Employee(employee=user,job_title=self.cleaned_data.get('job_title'))
        employee.save()
        return user