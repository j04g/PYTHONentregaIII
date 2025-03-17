from django.contrib import admin
from .models import Autor, Post, Comentario

# Registrar modelos en el admin
admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Comentario)

