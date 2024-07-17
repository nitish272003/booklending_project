from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'price', 'book_image', 'seller_name', 'location', 'phone_number','email',]
        labels = {
            'book_name': 'Book Name',
            'price': 'Price',
            'book_image': 'Book Image',
            'seller_name': 'Seller Name',
            'location': 'Location',
            'phone_number': 'Phone Number',
            'email': 'Email'
        }
        widgets = {
            'book_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
