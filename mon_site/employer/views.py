from django.shortcuts import render,redirect , get_object_or_404
from employer.models import Employer

from .form import EmployerForm



def liste_employer(request):
    employers=Employer.objects.all()
    
    return render(request,'employer/liste.html', {'employers':employers}) 

def ajouter_employer(request):
    form=EmployerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employer')  
    return render(request, 'employer/formulaire.html',{'forms':form})

def modifier_employer(request,id):
    employer=get_object_or_404(Employer,id=id)
    form=EmployerForm(request.POST or None, instance=employer)
    if form.is_valid():
        form.save()
        return redirect('liste_employer')
    return render(request, 'employer/formulaire.html',{'forms':form})

def suprimer_employer(request,id):
    employer=get_object_or_404(Employer,id=id)
    if request.method=='POST':
        employer.delete()
        return redirect('liste_employer')
    return render(request, 'employer/confim_suprim.html',{'employe':employer})
        
    
    
    
