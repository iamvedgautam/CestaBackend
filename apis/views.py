from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apis.serializer import CestaSerializer


class CestaViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        sez = CestaSerializer(data={
            **data,
            'created_by': request.user.pk,
        })
        if sez.is_valid():
            sez.save()
            return Response({'message': 'Created Cesta'}, status=status.HTTP_200_OK)
        return Response({'message': 'Validation Faild'}, status=status.HTTP_400_BAD_REQUEST)
        

    def list(self, request):
        
        return Response({'msg': 'get'}, status=status.HTTP_200_OK)
