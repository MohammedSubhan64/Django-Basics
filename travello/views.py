from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dist1=Destination()
    dist1.name="Hyderabad"
    dist1.title="A City of Diamond and Stones "
    dist1.img="static/images/destination_10.jpg"
    dist1.price=500

    dist2=Destination()
    dist2.name="Bangalore"
    dist2.title="The Future City  "
    dist2.img="static/images/destination_1.jpg"
    dist2.price=1100
    dists=[dist1,dist2]
    return render(request,'index.html',{'dists':dists})