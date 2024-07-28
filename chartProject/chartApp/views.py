from django.http import JsonResponse
from django.shortcuts import render

from chartApp.models import SalesData

# Create your views here.

def home(request):
    return render(request, 'chartApp/home.html')

def get_chart_data(request, chart_type):
    if chart_type == 'radar' or chart_type== 'bar' or chart_type== 'polar' \
    or chart_type== 'line' or chart_type== 'pie' or chart_type=='histogram' \
    or chart_type== 'doughnut':
        sales_data = list(SalesData.objects.values('month', 'sales'))
        chart_data = {'labels': [entry['month'] for entry in sales_data],
                      'data': [entry['sales'] for entry in sales_data]}
    
    return JsonResponse(chart_data)