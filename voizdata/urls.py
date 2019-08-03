from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index , name="home"),
    path('plans/',views.PlanList.as_view(),name="plans"),
    path('plans/view/<int:pk>/', views.PlanDetailsView.as_view(), name='detail'),
    path('plans/delete/<int:pk>/', views.PlanDestroyView.as_view(), name='delete'),
    path('plans/update/<int:pk>/', views.PlanUpdateView.as_view(),name='update'),
    path('plans/add/', views.PlanCreateView.as_view(),name='create')
]
