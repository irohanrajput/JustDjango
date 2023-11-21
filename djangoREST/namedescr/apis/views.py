from rest_framework import viewsets
from .serializers import justSerializer
from .models import justModel



class justViewSet(viewsets.ModelViewSet):
	queryset = justModel.objects.all()

	serializer_class = justSerializer
