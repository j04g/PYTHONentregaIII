from django.shortcuts import render, redirect
from .models import Autor, Post, Comentario
from .forms import AutorForm, PostForm, ComentarioForm

# Página de inicio con lista de posts
def inicio(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(titulo__icontains=query) | Post.objects.filter(contenido__icontains=query)
    else:
        posts = Post.objects.all().order_by('-fecha_publicacion')

    return render(request, 'blog/inicio.html', {'posts': posts, 'query': query})


# Vista para ver el detalle de un post
def detalle_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})


# Vista para agregar un autor
def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a la página principal
    else:
        form = AutorForm()
    return render(request, 'blog/agregar_autor.html', {'form': form})

# Vista para agregar un post
def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # ¡IMPORTANTE!
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/agregar_post.html', {'form': form})


# Vista para agregar un comentario
def agregar_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ComentarioForm()
    return render(request, 'blog/agregar_comentario.html', {'form': form})


from django.shortcuts import get_object_or_404

# Vista para editar un post
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_post.html', {'form': form, 'post': post})

# Vista para eliminar un post
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('inicio')
    return render(request, 'blog/eliminar_post.html', {'post': post})

