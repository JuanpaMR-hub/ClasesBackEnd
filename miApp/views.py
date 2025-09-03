from django.shortcuts import render

productos_list = [
    {"id":1,"nombre":"Super producto 1","precio":19.988},
    {"id":2,"nombre":"Producto Regular 2","precio":13.999},
    {"id":3,"nombre":"Producto Malo","precio":1}

]

def main(request):
    return render(request,'home.html')

def productos(request):
    context = {}
    context['mensaje'] = "Este es un mensaje!"
    context['productos'] = productos_list
    return render(request,'productos.html',context)

def detalle_producto(request,id):
    producto = None
    for p in productos_list:
        if p['id'] == id:
            producto = p
    return render(request, 'detalle_producto.html',{'producto':producto})
