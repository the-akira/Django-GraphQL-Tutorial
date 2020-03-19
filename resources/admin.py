from django.contrib import admin
from resources.models import Artista, Disco

classes = [Artista, Disco]

for c in classes:
	admin.site.register(c)