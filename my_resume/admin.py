from django.contrib import admin
from .models import Person, Skills, Languages, Awards, Education, Experience, Project
# Register your models here.
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Skills)
admin.site.register(Languages)
admin.site.register(Awards)
admin.site.register(Education)
admin.site.register(Experience)
