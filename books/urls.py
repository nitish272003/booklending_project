from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('sell/', views.sell, name='sell'),
    path('buy/', views.display_book, name='buy'),
    path('detail/<int:book_id>/',views.book_details, name = 'bookdetail'),
    path('contactus/<int:book_id>/', views.contactus, name='contactseller'),
]
