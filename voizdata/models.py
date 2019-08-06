from django.db import models

# Create your models here.
class LoginData(models.Model):
    username=models.CharField(max_length=150,blank=False, null=False)
    mobile=models.CharField(max_length=10,null=False)
    email=models.CharField(max_length=200,blank=False, null=False)
    password=models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        return self.username

PLAN_TYPE = [
    ('prepaid-plan-type','PREPAID'),
    ('postpaid-plan-type','POSTPAID'),
    ('dongle-plan-type','DONGLE'), ]

class ProfileData(models.Model):
    mobile=models.ForeignKey('LoginData',related_name='login',on_delete=models.CASCADE,null=False)
    active_plan = models.ForeignKey("Plan", related_name='plan', on_delete=models.CASCADE)
    user_type = models.CharField(choices=PLAN_TYPE,max_length=100)
    dob = models.DateField('DOB', auto_now_add=False)
    last_login = models.DateTimeField('Last_Login', auto_now_add=False)
    
    def __str__(self):
        return str(self.mobile)

class Plan(models.Model):
    plan_type=models.CharField(choices=PLAN_TYPE,max_length=100)
    name= models.CharField(max_length=100,blank=False, null=False)
    price=models.IntegerField(default=0,blank=False, null=False)
    validity=models.IntegerField(default=0,blank=False, null=False)
    description=models.CharField(max_length=200,blank=True, null=False)

    def __str__(self):
        return self.name
NUMBERS = (
    ('9876543210',9876543210),
    ('7871180868',7871180868),
    ('7871180867',7871180867),
    ('7871180866',7871180866),
    ('7871180865',7871180865),   
)
class NewConnection(models.Model):
    connection_type=models.CharField(choices=PLAN_TYPE,max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    pincode=models.BigIntegerField(default=600001)
    choose_number = models.CharField(choices=NUMBERS,max_length=12)
    
    def __str__(self):
        return self.name
    
class Recharge(models.Model):
    mobile=models.CharField(max_length=10)
    amount=models.IntegerField(default=0)
    time_recharged= models.DateTimeField(auto_now_add=False)
    
    def __str__():
        return self.mobile