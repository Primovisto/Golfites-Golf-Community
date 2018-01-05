from django.shortcuts import render, get_object_or_404
from .models import Equipment


def all_equipment(request):
    equipment = Equipment.objects.all()
    return render(request, "equipment/equipment.html", {"equipment": equipment})


def equipment_page(request, id):
    equipment = get_object_or_404(Equipment, pk=id)
    equipment.views += 1
    equipment.save()
    return render(request, "equipment/equipmentpage.html", {"equipment": equipment})
