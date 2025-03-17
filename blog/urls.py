from django.urls import path
from .views import inicio, agregar_autor, agregar_post, agregar_comentario, detalle_post, editar_post, eliminar_post

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar-autor/', agregar_autor, name='agregar_autor'),
    path('agregar-post/', agregar_post, name='agregar_post'),
    path('agregar-comentario/', agregar_comentario, name='agregar_comentario'),
    path('post/<int:post_id>/', detalle_post, name='detalle_post'),
    path('post/<int:post_id>/editar/', editar_post, name='editar_post'),
    path('post/<int:post_id>/eliminar/', eliminar_post, name='eliminar_post'),
]
