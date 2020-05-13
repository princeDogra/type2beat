from rest_framework.generics import ListAPIView
from dashboard.serializers import FoodItemSerializer
from dashboard.models import FoodItem, MedicalRecord
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

class FoodItemList(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('product_name',)

class MedicalChartData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def generate_data(self, request):
        queryset = MedicalRecord.objects.filter(user=request.user).order_by('timestamp')
        data = {'labels':[], 'Fasting Plasma Glucose': [], '2-h Plasma Glucose':[], 'HbA1c': []}
        for items in queryset:
            data['labels'].append(str(items.timestamp))
            data['Fasting Plasma Glucose'].append(items.fasting_plasma_glucose)
            data['2-h Plasma Glucose'].append(items.h2_plasma_glucose)
            data['HbA1c'].append(items.hbA1c)
        return data

    def get(self, request, format=None):
        data = self.generate_data(request)
        labels = data['labels']
        default_items = [
        {
            'label': 'Fasting Plasma Glucose',
            'backgroundColor': 'rgba(0, 63, 92, 1)',
            'data': data['Fasting Plasma Glucose']
        },
        {
            'label': "2-h Plasma Glucose",
            'backgroundColor': 'rgba(188, 80, 144, 1)',
            'data': data['2-h Plasma Glucose']
        },
        {
            'label': "HbA1c",
            'backgroundColor': 'rgba(255, 166, 0, 1)',
            'data': data['HbA1c']
        }]
        data = {
            "labels": labels,
            "datasets": default_items,
        }
        return Response(data)
