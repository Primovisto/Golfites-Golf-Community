from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Equipment


def all_equipment(request):
    equipment = Equipment.objects.all()
    return render(request, "equipment/equipment.html", {"equipment": equipment})


def equipment_page(request, id):
    equipment = get_object_or_404(Equipment, pk=id)
    equipment.views += 1
    equipment.save()
    return render(request, "equipment/equipmentpage.html", {"equipment": equipment})


def search_names(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    equipment = Equipment.objects.filter(name__contains=search_text)

    return render_to_response('ajax_search.html', {'equipment': equipment})
