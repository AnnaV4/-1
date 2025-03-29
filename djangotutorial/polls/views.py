from rest_framework import viewsets
from .serializers import OperationSerializer
from .models import Operation

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer