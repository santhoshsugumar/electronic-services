from django.contrib import admin
from electro_app.models import customer_request,customer_message,subscriber,review
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(customer_request)
admin.site.register(customer_message)
admin.site.register(subscriber)
admin.site.register(review)

