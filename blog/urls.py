from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView
from django.urls import path

urlpatterns = [
    path('',BlogListView.as_view(), name='home'), 

    path('post/<int:pk>',BlogDetailView.as_view(),name='post_details'),

    path('post/new',BlogCreateView.as_view(),name='post_create'),

    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name='post_update'),

    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),

    ]
    

