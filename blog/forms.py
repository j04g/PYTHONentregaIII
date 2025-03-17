from django import forms
from .models import Autor, Post, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'biografia']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'imagen']  # Agregamos "imagen"


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['post', 'autor', 'contenido']
