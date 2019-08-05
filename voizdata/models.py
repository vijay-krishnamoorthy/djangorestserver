from django.db import models

# Create your models here.
class LoginData(models.Model):
    username=models.CharField(max_length=150,blank=False, null=False)
    mobile=models.CharField(max_length=10,blank=False, null=False)
    email=models.CharField(max_length=200,blank=False, null=False)
    password=models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        return self.username

PLAN = (
    ('prepaid-plan-type','PREPAID'),
    ('postpaid-plan-type','POSTPAID'),
    ('dongle-plan-type','DONGLE')
)
class ProfileData(models.Model):
    user = models.ForeignKey('LoginData', related_name='profile', on_delete=models.CASCADE)
    active_plan = models.ForeignKey("Plan", related_name='plans', on_delete=models.CASCADE)
    user_type= models.CharField(choices= PLAN,max_length=100)
    data_remaining= models.IntegerField(default=0)
    calls_remaining=models.IntegerField(default=0)
    balance = models.IntegerField(default=5)
    dob = models.DateField(auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Plan(models.Model):
    plan_type=models.CharField(choices=PLAN,max_length=100)
    name= models.CharField(max_length=100,blank=False, null=False)
    price=models.IntegerField(default=0,blank=False, null=False)
    validity=models.IntegerField(default=0,blank=False, null=False)
    description=models.CharField(max_length=200,blank=True, null=False)

    def __str__(self):
        return self.name

