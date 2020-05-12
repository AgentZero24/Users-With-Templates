from django.shortcuts import render, redirect

# Create your views here.
from .models import Users
# show all of the data from a table
def index(request):
    context = {
    	"Users": Users.objects.all()
    }
    return render(request, "index.html", context)
def addUser(request):
    addUser1 = Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age'],
    )
    return redirect(f"/")
