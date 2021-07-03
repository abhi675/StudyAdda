from django.contrib import admin
from .models import Courses,Payment, Faculty,Contact
# Register your models here.
admin.site.register(Courses)
admin.site.register(Faculty)
admin.site.register(Payment)
admin.site.register(Contact)