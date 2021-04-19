from django.contrib import admin
from .models import Sith, Recruit, Planet, Question, HandShadow

# Register your models here.

admin.site.register(Sith)
admin.site.register(Recruit)
admin.site.register(Planet)
admin.site.register(Question)
admin.site.register(HandShadow)