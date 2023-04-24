from django.urls import path
from .views import CustomerList, RecommendationList, RecommendationDetail

urlpatterns = [
    path("customers/", CustomerList.as_view()),
    path("recommendations/", RecommendationList.as_view()),
    path("recommendations/<int:pk>/", RecommendationDetail.as_view()),
]
