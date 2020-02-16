from django.urls import path
from MainApp import views

urlpatterns = [
	path('', views.index, name='homepage'),
	path('signup/', views.sign_up, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('change_passwd/', views.change_password, name='change_password'),
	path('add/', views.add_book, name='add_book'),
	path('upload_image/', views.add_image, name='add_image'),
	path('list/<str:category>/', views.book_list, name='book_list'),
	path('detail/<int:book_id>/', views.book_detail, name='book_detail'),
	]





