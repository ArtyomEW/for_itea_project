from django.contrib import admin
from .models import Listeners,Application,Mentors,Groups,Course
# Register your models here.
admin.site.register(Listeners)
admin.site.register(Application)
admin.site.register(Mentors)
admin.site.register(Groups)
admin.site.register(Course)