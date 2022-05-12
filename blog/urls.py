from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_list_url'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail_url'),
    path('add/', views.AddBlogView.as_view(), name='add_blog_url'),
    path('update/<int:pk>/', views.UpdateBlogView.as_view(), name='update_blog_url'),
    path('delete/<int:pk>/', views.delete_blog_response, name='delete_blog_url'),
]
