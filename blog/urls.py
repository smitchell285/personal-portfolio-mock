from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('',views.Blogs,name='blogs'),
    path('blog/<int:pk>/',views.BlogDetail.as_view(),name='blog_detail'),
]
