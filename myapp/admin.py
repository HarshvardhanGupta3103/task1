from django.contrib import admin
from .models import Client, Project, Newsletter, Contact

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Newsletter)
admin.site.register(Contact)
