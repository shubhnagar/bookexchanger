from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from .models import Books
from django.utils import timezone 
# Create your views here.
def home(request): 
 return render(request, 'books/home.html')



def create (request):
   if request.method == 'POST': 
    if request.POST['subject'] and request.POST['name'] and request.POST['date'] and request.FILES['image'] :
     books = Books() 
     books.subject = request.POST['subject']   
     books.name = request.POST['name']  
     books.image = request.FILES['image'] 
     books.date = timezone.datetime.now()  
     books.save() 
     return redirect('home')       
 
 
    else: 
     return render(request, 'books/create.html',{'error':'All field required'})   
   else: 
    return render(request, 'books/create.html') 