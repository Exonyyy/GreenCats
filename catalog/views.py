from django.shortcuts import render
from .models import *


def catalog(request):
    structures = BankProtectionStructures.objects.all()
    context = {
        "structures": structures
    }
    return render(request, 'catalog.html', context)


def structure_info(request, name):
    structure = BankProtectionStructures.objects.get(name=name)
    context = {
        "structure": structure
    }
    return render(request, 'structure_info.html', context)
