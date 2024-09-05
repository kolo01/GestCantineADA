from django.shortcuts import redirect, render

from dishes.forms import DishesForm
from dishes.models import DishesModel
from menu.models import MenuModel


# Create your views here.

def home(request):
    all_dishes = DishesModel.objects.all()
    all_menu = MenuModel.objects.all()
    total_menu = all_menu.count()
    total_dishes = all_dishes.count()
    return render(request, 'index.html', {"total_menu":total_menu,"total_dishes":total_dishes})


def list_dishes(request):
    search_field = request.GET.get('search')
    if search_field:
        founded_dishes = DishesModel.objects.filter(name__icontains=search_field)
        total = founded_dishes.count()

        return render(request, 'dishes/list.html', {'all_dishes': founded_dishes, 'total': total, 'search_field':search_field})
    else:
        all_dishes = DishesModel.objects.all()
        total = all_dishes.count()
        return render(request, 'dishes/list.html', {'all_dishes': all_dishes, 'total': total})


def add_edit_dishes(request,id=None):
    if id:
        dishes_selected = DishesModel.objects.get(id=id)
        dishes_form = DishesForm(instance=dishes_selected)
        if request.method == 'POST':
            form = DishesForm(request.POST, instance=dishes_selected)
            if form.is_valid():
                form.save()
                return redirect('dishes:index')
        return render(request, 'forms.html', {'dishes_form': dishes_form,'title':"Modification d'un plat"})
    else:
        dishes_form = DishesForm()
        if request.method == 'POST':
            form = DishesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dishes:index')
            else:
                print("Error")
        # return render(request, 'dishes/add_edit_dishes.html', {'dishes_form': dishes_form,'title':"Ajout d'un dishes"})
        return render(request, 'forms.html', {'dishes_form': dishes_form,'title':"Ajout d'un palt"})
    

def delete_dishes(request, id):
    dishes_to_delete = DishesModel.objects.get(id=id)
    dishes_to_delete.delete()
    return redirect('dishes:index')