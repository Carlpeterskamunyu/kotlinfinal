from django.contrib import admin
from myapp.models import User, Product, Appointments, Member  # Import the User model from models.py
from .models import Contact
# Register the User model with the admin site
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Appointments)
admin.site.register(Contact)
admin.site.register(Member)