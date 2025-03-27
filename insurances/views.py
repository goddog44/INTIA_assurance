from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Insurance
from .forms import InsuranceForm

@login_required
def insurance_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        insurances = Insurance.objects.filter(
            Q(policy_number__icontains=search_query) | 
            Q(client__name__icontains=search_query) |
            Q(type__icontains=search_query)
        )
    else:
        insurances = Insurance.objects.all()
    
    # Filter by user's branch unless they're from headquarters
    if request.user.branch != 'headquarter':
        insurances = insurances.filter(client__branch=request.user.branch)
    
    return render(request, 'insurances/insurance_list.html', {
        'insurances': insurances,
        'search_query': search_query
    })

@login_required
def insurance_detail(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    
    # Check if user has access to this insurance
    if request.user.branch != 'headquarter' and request.user.branch != insurance.client.branch:
        messages.error(request, "Vous n'avez pas accès à cette assurance.")
        return redirect('insurance_list')
    
    return render(request, 'insurances/insurance_detail.html', {
        'insurance': insurance
    })

@login_required
def insurance_create(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST, user=request.user)
        if form.is_valid():
            insurance = form.save(commit=False)
            insurance.created_by = request.user
            
            # Check if user has access to selected client
            if request.user.branch != 'headquarter' and request.user.branch != insurance.client.branch:
                messages.error(request, "Vous n'avez pas accès à ce client.")
                return redirect('insurance_list')
                
            insurance.save()
            messages.success(request, "Assurance ajoutée avec succès.")
            return redirect('insurance_detail', pk=insurance.pk)
    else:
        form = InsuranceForm(user=request.user)
    
    return render(request, 'insurances/insurance_form.html', {
        'form': form,
        'title': 'Ajouter une assurance'
    })

@login_required
def insurance_update(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    
    # Check if user has access to this insurance
    if request.user.branch != 'headquarter' and request.user.branch != insurance.client.branch:
        messages.error(request, "Vous n'avez pas accès à cette assurance.")
        return redirect('insurance_list')
    
    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance, user=request.user)
        if form.is_valid():
            # Check if user has access to selected client
            if request.user.branch != 'headquarter' and request.user.branch != form.cleaned_data['client'].branch:
                messages.error(request, "Vous n'avez pas accès à ce client.")
                return redirect('insurance_detail', pk=insurance.pk)
                
            form.save()
            messages.success(request, "Assurance modifiée avec succès.")
            return redirect('insurance_detail', pk=insurance.pk)
    else:
        form = InsuranceForm(instance=insurance, user=request.user)
    
    return render(request, 'insurances/insurance_form.html', {
        'form': form,
        'insurance': insurance,
        'title': 'Modifier une assurance'
    })

@login_required
def insurance_delete(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    
    # Check if user has access to this insurance
    if request.user.branch != 'headquarter' and request.user.branch != insurance.client.branch:
        messages.error(request, "Vous n'avez pas accès à cette assurance.")
        return redirect('insurance_list')
    
    if request.method == 'POST':
        insurance.delete()
        messages.success(request, "Assurance supprimée avec succès.")
        return redirect('insurance_list')
    
    return render(request, 'insurances/insurance_confirm_delete.html', {
        'insurance': insurance
    })