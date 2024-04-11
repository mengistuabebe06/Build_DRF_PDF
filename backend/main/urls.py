from django.urls import path
from .views import process_pdf, get_extracted_data

urlpatterns = [
    path("extracted_data/", get_extracted_data, name="get_extracted_data"),
    path("process_pdf/", process_pdf, name="process-pdf"),
]
