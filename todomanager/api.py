from todomanager.models import Todo
from rest_framework import viewsets,permissions
from .serializer import TodoSerializer

# Todo viewset
class TodoViewSet(viewsets.ModelViewSet):
    # specify a queryset that is going to take all model objects
    # queryset = Todo.objects.all()
    # set permissions

    permission_classes = [
        permissions.IsAuthenticated
    ]

     # pass the serializer class
    serializer_class = TodoSerializer

    # methods to return todos for a specific user
    def get_queryset(self):
        return self.request.user.todos.all()

    # create a todo based on a user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    