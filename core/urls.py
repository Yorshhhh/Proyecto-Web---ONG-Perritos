from django.urls import path
from .views import home, inscripcion, productos, quienessomos, Lista_Producto, aniadir_producto, \
modificar_producto, eliminar_producto, registro, tienda

urlpatterns = [
    path('', home,name="home"),
    path('inscripcion/', inscripcion,name="inscripcion"),
    path('productos/', productos,name="productos"),
    path('quienessomos/', quienessomos,name="quienessomos"),
    path('Lista_Producto/', Lista_Producto,name="Lista_Producto"),
    path('aniadir_producto/', aniadir_producto,name="aniadir_producto"),
    path('modificar_producto/<id>/', modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto,name="eliminar_producto"),
    path('registro/', registro,name="registro"),
    path('', tienda, name="tienda"),
]