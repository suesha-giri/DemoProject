from .models import City
from .serializers import PlacesCreateSerializer, PlacesListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class PlacesViewSet(ModelViewSet):
    queryset = City.objects.select_related('country').filter(is_obsolete=False).order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'create':
            return PlacesCreateSerializer
        return PlacesListSerializer 

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_obsolete = True
        obj.save(update_fields=['is_obsolete', 'updated_at'])
        return Response({"message": "Deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)