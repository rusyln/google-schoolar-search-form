from django.urls import path
from .views import SearchProfileView , home_view , ProfileDetailView

urlpatterns = [
     path('', home_view, name='home'),
    path('search-profile/', SearchProfileView.as_view(), name='search_profile'),
     path('profile/<str:author_id>/', ProfileDetailView.as_view(), name='profile_detail'),
  
]
