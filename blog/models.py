from django.db import models

# Modelo para los autores
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo para los posts
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.titulo

# Modelo para los comentarios
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.post.titulo}'
