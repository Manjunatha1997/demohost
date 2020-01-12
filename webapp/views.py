from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def greetings(request):
    if request.method == 'POST':
        name=request.POST['name']

    return render(request,'result.html',{'name':name})
