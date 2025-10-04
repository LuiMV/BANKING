from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Countries
from .forms import CountryForm

def country_list(request):
    countries = Countries.objects.all().order_by("name") 

    paginator = Paginator(countries, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    return render(request, "banking_app/country_list.html", {"page_obj": page_obj})


def country_edit(request, pk):
    countries = get_object_or_404(Countries, pk=pk)

    if request.method == 'POST':
        form = CountryForm(request.POST, instance=countries)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('country_list')
    else:
        form = CountryForm(instance=countries)

    return render(request, 'banking_app/country_form.html', {'form': form, 'countries': countries})
   
    