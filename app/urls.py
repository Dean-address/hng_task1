from django.urls import path
from .api.views import NumberView

urlpatterns = [
    path("classify-number", NumberView.as_view(), name="number"),
]
