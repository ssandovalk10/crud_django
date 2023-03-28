from django.views.generic import ListView

from .models import Curso

class CursoListView(ListView):
    model=Curso
    
    def get_queryset(self):
        return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Gestion de Cursos'
        return context
    
def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')