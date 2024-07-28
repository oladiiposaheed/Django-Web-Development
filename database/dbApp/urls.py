from django.urls import path
from dbApp import views

urlpatterns = [
    path('category', views.Showcategories, name='category'),
    path('showorder', views.rawSql, name='showorder'),
    path('storedprocedure', views.storedProcedureSQl, name='storedProcedure'),
    path('storewthoutpro', views.storedProcedureWithoutOutputParameters, name='storewthoutpro'),
    path('Export_to_csv', views.exporttoCSV, name='export_to_csv'),
    path('Export_json', views.exporttoJSON, name='export_to_json'),
    path('export_xlsl', views.exportToXLS, name='export_to_excel'),
    path('export_word', views.exportToWord, name='export_to_word'),
    path('export_pdf', views.exportPdf, name='export_to_pdf')
]
