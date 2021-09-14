from django.urls import path
from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    #path('project/<int:pk>/',views.ProjectDetail.as_view(),name='project_detail'),
]
