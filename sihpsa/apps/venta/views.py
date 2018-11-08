from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.venta.models import Articulo, Categoria
from apps.venta.forms import ArticuloForm
# Create your views here.


def buscar(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all()
    error = False
    if 'busart' in request.GET:
        busqueda = request.GET['busart']
        if not busqueda:
            error = True
        else:
            articulos = Articulo.objects.filter(
                nombre_articulo__icontains=busqueda)
            categorias = Categoria.objects.all()
            contexto = {'articulos_mostrar': articulos,
                        'categorias': categorias}
            return render(request, 'venta/articulo_list.html', contexto)

        contexto = {'articulos_mostrar': articulos,
                    'categorias': categorias, 'error': error}
        return render(request, 'venta/articulo_list.html', contexto)

    # Obtengo el nombre del boton(categoria) para obtener el listado de todos los articulos de dicha categoria
    for i in range(0, len(categorias)):
        if categorias[i].nombre_categoria in request.GET:
            cate = Categoria.objects.get(
                nombre_categoria=categorias[i].nombre_categoria)

            art = Articulo.objects.filter(categoria=cate.id)
            contexto = {'articulos_mostrar': art,
                        'categorias': categorias}
            return render(request, 'venta/articulo_list.html', contexto)
    else:
        articulos = Articulo.objects.all()
        contexto = {'articulos_mostrar': articulos, 'categorias': categorias}
        return render(request, 'venta/articulo_list.html', contexto)


def editar(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    if request.method == 'GET':
        form=ArticuloForm(instance=articulo)
    else:
        form=ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('inventario_url:listar')

    contexto={'form':form}     
    return render(request, 'venta/crearArticulo.html',contexto)


class ArticuloCreate(CreateView):
    model=Articulo
    form_class=ArticuloForm
    template_name='venta/crearArticulo.html'
    success_url=reverse_lazy('inventario_url:listar')
