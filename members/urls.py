from django.urls import path
from .views import SearchProfileView

urlpatterns = [
    path('search-profile/', SearchProfileView.as_view(), name='search_profile'),
  
]
