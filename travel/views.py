from django.shortcuts import render
from .models import Destination

# 1.Create your views here.
# def index(request):
#     desc1 = Destination()
#     desc1.name = "Mumbai"
#     desc1.desc = "The city that never sleep"
#     desc1.price = 701
#     desc1.img = 'destination_1.jpg'
#     desc1.offer = False
#     desc2 = Destination()
#     desc2.name = "Hyderabad"
#     desc2.desc = "First Biryani the Lithi chokha"
#     desc2.price = 401
#     desc2.img = 'destination_2.jpg'
#     desc2.offer = True
#     desc3 = Destination()
#     desc3.name = "Bengaluru"
#     desc3.desc = "The city is selecon city"
#     desc3.price = 751
#     desc3.img = 'destination_3.jpg'
#     desc3.offer = False

#     # return render(request, 'index.html',{'desc1':desc1, 'desc2':desc2, 'desc3':desc3})

#     dests = [desc1, desc2, desc3]
#     return render(request, 'index.html',{'dests':dests})
# 1.Create your views here.
def index(request):

    dests = Destination.objects.all() 
    return render(request, 'index.html',{'dests':dests})

