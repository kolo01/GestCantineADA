from django.shortcuts import redirect, render

from dishes.models import DishesModel
from menu.forms import MenuForm
from menu.models import MenuModel

# Create your views here.

def list_menu(request):
    search_field = request.GET.get('search')
    if search_field:
        founded_menu = MenuModel.objects.filter(id__icontains=search_field)
        total = founded_menu.count()

        return render(request, 'dishes/list.html', {'all_menu': founded_menu, 'total': total, 'search_field':search_field})
    else:
        all_menu = MenuModel.objects.all()
        all_dishes = DishesModel.objects.all()
        total = all_menu.count()
        return render(request, 'menu/list.html', {'all_menu': all_menu, 'all_dishes': all_dishes,'total': total})

def add_edit_menu(request,id=None):
    if id:
        menu_selected = MenuModel.objects.get(id=id)
        menu_form = MenuForm(instance=menu_selected)
        if request.method == 'POST':
            form = MenuForm(request.POST, instance=menu_selected)
            if form.is_valid():
                form.save()
                return redirect('menu:index')
        # return render(request, 'menu/add_edit_menu.html', {'menu_form': menu_form,'title':"Modification du menu"})
        return render(request, 'forms.html', {'menu_form': menu_form,'title':"Modification du menu"})

    else:
        menu_form = MenuForm()
        if request.method == 'POST':
            form = MenuForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('menu:index')
        # return render(request, 'menu/add_edit_menu.html', {'menu_form': menu_form,'title':"Ajout d'un menu"})
        return render(request, 'forms.html', {'menu_form': menu_form,'title':"Ajout du menu"})
        
    

def delete_menu(request, id):
    menu_to_delete = MenuModel.objects.get(id=id)
    menu_to_delete.delete()
    return redirect('menu:index')