from django.urls import path

from .views import CursoListView, registrar_curso, eliminar_curso

urlpatterns = [
    path('', CursoListView.as_view(), name="gestion_cursos"),
    path('registrarCurso', registrar_curso),
    path('eliminarCurso/<int:id>', eliminar_curso),
]
