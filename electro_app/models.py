from django.db import models
from django.contrib.auth.models import User
#import user model 

# Create your models here.


request_type=(
     ("--PLEASE CHOOSE A SERVICE--","--Please choose a service--"),
     ("laptop","LAPTOP"),
    ("tv","TV"),
     ("smart phone","SMART PHONE"),
     ("wifi","WIFI"),
     ("ac","AC"),
 )

class customer_request(models.Model):
    customer_name=models.CharField(max_length=20)
    email_ID=models.EmailField()
    phone_number=models.IntegerField()
    address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pin_code=models.IntegerField()
    request_Type=models.CharField(max_length=50, choices=request_type, default=" ")
    description=models.TextField()
    date=models.CharField(max_length=20)
    connect=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)
    cdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
    
    
    
class customer_message(models.Model):
    name=models.CharField(max_length=20)
    email_ID=models.EmailField()
    phone_number=models.IntegerField()
    subject=models.CharField(max_length=20)
    message=models.TextField()
    author=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class subscriber(models.Model):
    email_ID =models.EmailField()


    def __str__(self):
        return self.email_ID
    
    
    

class review(models.Model):
     review_message=models.TextField()
     boss=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

     def __str__(self):
        return self.boss.first_name 