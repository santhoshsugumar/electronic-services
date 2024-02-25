from django.forms import ModelForm
from electro_app.models import customer_request,customer_message,subscriber,review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your Model forms

class customer_request_form(ModelForm):
    class Meta:
        model=customer_request
        fields=['customer_name','email_ID','phone_number','address','city','state','pin_code','request_Type','description','date']


class customer_message_form(ModelForm):
    class Meta:
        model=customer_message
        fields=['name','email_ID','phone_number','subject','message']


class subscriber_form(ModelForm):
    class Meta:
        model=subscriber
        fields=['email_ID']


class review_form(ModelForm):
    class Meta:
        model=review
        fields=['review_message']

class register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']