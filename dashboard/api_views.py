from rest_framework.generics import ListAPIView, CreateAPIView
from dashboard.serializers import FoodItemSerializer, NutritionIntakeSerializer, MedialRecordSerializer
from dashboard.models import FoodItem, MedicalRecord, NutritionIntake
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class FoodItemList(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('product_name','=id')

class MedicalData(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MedialRecordSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user).order_by('-timestamp')
        return queryset

class NutritionIntakeData(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NutritionIntakeSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user).order_by('-timestamp')
        print(queryset)
        return queryset

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


class NutritionIntakeChartData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def generate_data(self, request):
        queryset = NutritionIntake.objects.filter(user=request.user).order_by('timestamp')
        data = {'labels':[], 'productName':[],'sugar': [], 'fat':[], 'carbohydrate': [], 'protein': []}
        for item in queryset:
            data['labels'].append(str(item.timestamp))
            data['productName'].append(item.food.product_name)
            data['sugar'].append(item.food.sugars_100g)
            data['fat'].append(item.food.fat_100g)
            data['carbohydrate'].append(item.food.carbohydrates_100g)
            data['protein'].append(item.food.proteins_100g)
        return data

    def get(self, request, format=None):
        data = self.generate_data(request)
        labels = data['labels']
        default_items = [
        {
            'label': 'Sugar',
            'backgroundColor': 'rgba(0, 63, 92, 1)',
            'data': data['sugar']
        },
        {
            'label': "Carbs",
            'backgroundColor': 'rgba(122, 81, 149, 1)',
            'data': data['carbohydrate']
        },
        {
            'label': "Fat",
            'backgroundColor': 'rgba(239, 86, 117, 1)',
            'data': data['fat']
        },
        {
            'label': 'protein',
            'backgroundColor': 'rgba(255, 166, 0, 1)',
            'data': data['protein']
        }]
        data = {
            "labels": labels,
            "datasets": default_items,
        }
        return Response(data)
