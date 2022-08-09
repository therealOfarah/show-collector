from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('shows/', views.shows_index, name='shows_index'),
  path('shows/<int:show_id>/', views.shows_detail, name='shows_detail'),
  path('shows/create/', views.ShowCreate.as_view(), name="shows_create"),
  path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
  path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
  path('genre/create/', views.GenreCreate.as_view(), name='genre_create'),
  path('genre/<int:pk>/', views.GenreDetail.as_view(), name='genre_detail'),
  path('genre/', views.GenreList.as_view(), name='genre_index'),
  path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre_update'),
  path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
  path('accounts/signup/', views.signup, name='signup')
]