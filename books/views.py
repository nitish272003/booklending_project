from django.shortcuts import render,redirect
from .models import Book

from .forms import BookForm

def sell(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'sell.html', {'form': form})



def display_book(request):
    books = Book.objects.all()
    return render(request, 'buy.html', {'books': books})

def book_details(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    
    return render(request, 'bookDetail.html',{'book': book})



from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.conf import settings

def contactus(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Create a formal message using string formatting
        formal_message = f"Hey {book.seller_name},\n\n" \
                        f"I am interested in the book titled '{book.book_name}' you have listed for sale. " \
                        f"Here are my contact details:\n" \
                        f"Name: {name}\n" \
                        f"Email: {email}\n\n" \
                        f"Message:\n{message}"

        send_mail(
            'Contact Form Submission',
            formal_message,
            settings.EMAIL_HOST_USER,  # Use your email as the sender
            [book.email],  # Use the seller's email as the recipient
            fail_silently=False,
        )

        # Redirect to a success page or perform any other desired action
        return render(request, 'success.html')
    return render(request,'contactus.html',{'book':book})
