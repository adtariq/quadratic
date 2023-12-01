from django.contrib import messages
from django.shortcuts import render,redirect

import math
import matplotlib.pyplot as plt
# Create your views here.

def quadratic(request):
    context=dict()
    if request.method=="POST":
        a=int(request.POST.get('a'))
        b=int(request.POST.get('b'))
        c=int(request.POST.get('c'))
        d=b*b-4*a*c
        print("Descriminent",d)
        if d<0:
            messages.warning(request, 'Dear User insert accurate values! These are imaginary roots.')
            print("imaginary roots")
        else:
            x=((-b+math.sqrt(d))/2*a)
            y=((-b-math.sqrt(d))/2*a)
            print(x,y)
            context={'x':x,'y':y}
           
    print(context.keys())
    print(context.values())
    return render(request,"home.html",context)
   
