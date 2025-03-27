from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Client, Insurance, Branch
from .forms import LoginForm, ClientForm, InsuranceForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            branch_name = form.cleaned_data.get('branch')  # Get the selected branch name
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['branch_name'] = branch_name  # Store in session
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    branch_id = request.session.get('branch')
    branch = Branch.objects.get(id=branch_id) if branch_id else None
    return render(request, 'dashboard.html', {
        'branch': branch
    })

@login_required
def clients(request):
    branch_id = request.session.get('branch')
    clients = Client.objects.filter(branch_id=branch_id)
    return render(request, 'clients.html', {
        'clients': clients
    })

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {
        'form': form,
        'client': client
    })

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {
        'form': form
    })

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')
    return render(request, 'client_confirm_delete.html', {
        'client': client
    })

@login_required
def insurances(request):
    branch_id = request.session.get('branch')
    insurances = Insurance.objects.filter(client__branch_id=branch_id)
    return render(request, 'insurances.html', {
        'insurances': insurances
    })

@login_required
def insurance_detail(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            form.save()
            return redirect('insurances')
    else:
        form = InsuranceForm(instance=insurance)
    return render(request, 'insurance_form.html', {
        'form': form,
        'insurance': insurance
    })

@login_required
def insurance_create(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            insurance = form.save(commit=False)
            insurance.created_by = request.user
            insurance.save()
            return redirect('insurances')
    else:
        form = InsuranceForm()
    return render(request, 'insurance_form.html', {
        'form': form
    })

@login_required
def insurance_delete(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    if request.method == 'POST':
        insurance.delete()
        return redirect('insurances')
    return render(request, 'insurance_confirm_delete.html', {
        'insurance': insurance
    })

@login_required
def get_clients_json(request):
    branch_id = request.session.get('branch')
    clients = Client.objects.filter(branch_id=branch_id).values('id', 'first_name', 'last_name')
    return JsonResponse(list(clients), safe=False)