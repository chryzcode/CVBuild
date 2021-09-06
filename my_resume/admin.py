from django.contrib import admin
from .models import Person, Skills, Awards, Education, Experience, Project, Volunteer
# Register your models here.
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Skills)
admin.site.register(Awards)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Volunteer)