from rest_framework import viewsets, generics
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaCursoSerializer, ListaMatriculaEstudanteSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaCursoSerializer