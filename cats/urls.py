from django.urls import path
from . import views


# https://docs.djangoproject.com/en/4.2/topics/http/urls/
app_name = 'cats'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),

]

# Note that make_ = breed_ and auto_= cat_ give us uniqueness within this application
