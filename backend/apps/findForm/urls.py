from django.urls import path
from .views import RetrieveFormView

urlpatterns = [
    path('get_form',RetrieveFormView.as_view())
]