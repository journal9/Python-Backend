from django.urls import path
from .views import CompressorView,MergeView

urlpatterns = [
    path('compress',CompressorView.as_view()),
    path('merge',MergeView.as_view()),
]