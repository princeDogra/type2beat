from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets
from rest_framework.response import Response

from dashboard.models import FoodItem, MedicalRecord
from .serializers import FoodItemSerializer, MedialRecordSerializer


class FoodItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

class MedicalRecordViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # serializer_class = MedialRecordSerializer
    # queryset = MedicalRecord.objects.all()

    def list(self, request):
        queryset = MedicalRecord.objects.filter(user=request.user)
        serializer = MedialRecordSerializer(queryset, many=True)
        return Response(serializer.data)
