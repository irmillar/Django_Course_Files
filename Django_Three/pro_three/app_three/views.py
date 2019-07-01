from django.shortcuts import render
from app_three.forms import SignUp

# Create an empty 'user' view to be connected to the users.html file
def index(request):
    return render(request, 'app_three/index.html')

def users(request):
    form = SignUp()

    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR: Invalid Form")

    return render(request, 'app_three/users.html', {'form':form})
