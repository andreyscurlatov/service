from django.contrib import admin
from .models import Sith, Recruit, Planet, Question

# Register your models here.

admin.site.register(Sith)
admin.site.register(Recruit)
admin.site.register(Planet)
#admin.site.register(Test)
admin.site.register(Question)