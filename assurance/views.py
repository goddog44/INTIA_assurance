from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib import messages
from .models import Succursale, Client, Assurance, TypeAssurance
from .forms import LoginForm, ClientForm, AssuranceForm
from django.db.models import Count, Sum

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            succursale_nom = form.cleaned_data.get('succursale')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Stocker à la fois le nom et l'ID de la succursale
                succursale = Succursale.objects.get(nom=succursale_nom)
                request.session['succursale_nom'] = succursale_nom
                request.session['succursale_id'] = succursale.id
                return redirect('tableau_de_bord')
            else:
                messages.error(request, "Identifiants incorrects.")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('login')

@login_required
def tableau_de_bord(request):
    succursale_id = request.session.get('succursale_id')
    stats = {
        'nb_clients': Client.objects.filter(succursale_id=succursale_id).count(),
        'nb_assurances': Assurance.objects.filter(client__succursale_id=succursale_id).count(),
        'montant_total': Assurance.objects.filter(client__succursale_id=succursale_id)
                         .aggregate(total=Sum('montant'))['total'] or 0
    }
    return render(request, 'dashboard.html', {
        'succursale': request.session.get('succursale_nom'),
        'stats': stats
    })

# Fonction utilitaire pour vérifier les permissions
def check_succursale_permission(user, succursale_id):
    if user.is_superuser or is_direction_generale(user):
        return True
    return str(user.profile.succursale.id) == str(succursale_id)

# Vues pour les clients
@login_required
def liste_clients(request):
    succursale_id = request.session.get('succursale_id')
    clients = Client.objects.filter(succursale_id=succursale_id)
    return render(request, 'list.html', {'clients': clients})

@login_required
def detail_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if not check_succursale_permission(request.user, client.succursale.id):
        messages.error(request, "Accès non autorisé.")
        return redirect('liste_clients')
    
    assurances = client.assurance_set.all()
    return render(request, 'detail_client.html', {
        'client': client,
        'assurances': assurances
    })

@login_required
def creer_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.succursale_id = request.session.get('succursale_id')
            client.created_by = request.user
            client.save()
            messages.success(request, "Client créé avec succès.")
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if not check_succursale_permission(request.user, client.succursale.id):
        messages.error(request, "Accès non autorisé.")
        return redirect('liste_clients')
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client mis à jour avec succès.")
            return redirect('liste_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form, 'client': client})

@login_required
def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if not check_succursale_permission(request.user, client.succursale.id):
        messages.error(request, "Accès non autorisé.")
        return redirect('liste_clients')
    
    if request.method == 'POST':
        client.delete()
        messages.success(request, "Client supprimé avec succès.")
        return redirect('liste_clients')
    return render(request, 'list.html', {'client': client})

# Vues pour les assurances
@login_required
def liste_assurances(request):
    succursale_id = request.session.get('succursale_id')
    assurances = Assurance.objects.filter(client__succursale_id=succursale_id)
    return render(request, 'list.html', {'assurances': assurances})

@login_required
def creer_assurance(request):
    succursale_id = request.session.get('succursale_id')
    if request.method == 'POST':
        form = AssuranceForm(succursale_id, request.POST)
        if form.is_valid():
            assurance = form.save(commit=False)
            assurance.created_by = request.user
            assurance.save()
            messages.success(request, "Assurance créée avec succès.")
            return redirect('liste_assurances')
    else:
        form = AssuranceForm(succursale_id)
    return render(request, 'assurances/formulaire.html', {'form': form})

@login_required
def modifier_assurance(request, pk):
    assurance = get_object_or_404(Assurance, pk=pk)
    if not check_succursale_permission(request.user, assurance.client.succursale.id):
        messages.error(request, "Accès non autorisé.")
        return redirect('liste_assurances')
    
    if request.method == 'POST':
        form = AssuranceForm(assurance.client.succursale.id, request.POST, instance=assurance)
        if form.is_valid():
            form.save()
            messages.success(request, "Assurance mise à jour avec succès.")
            return redirect('liste_assurances')
    else:
        form = AssuranceForm(assurance.client.succursale.id, instance=assurance)
    return render(request, 'assurances/formulaire.html', {'form': form, 'assurance': assurance})

@login_required
def supprimer_assurance(request, pk):
    assurance = get_object_or_404(Assurance, pk=pk)
    if not check_succursale_permission(request.user, assurance.client.succursale.id):
        messages.error(request, "Accès non autorisé.")
        return redirect('liste_assurances')
    
    if request.method == 'POST':
        assurance.delete()
        messages.success(request, "Assurance supprimée avec succès.")
        return redirect('liste_assurances')
    return render(request, 'assurances/supprimer.html', {'assurance': assurance})

# API
@login_required
def get_clients_json(request):
    succursale_id = request.session.get('succursale_id')
    clients = Client.objects.filter(succursale_id=succursale_id).values('id', 'prenom', 'nom')
    return JsonResponse(list(clients), safe=False)

# Fonction de vérification de permission
def is_direction_generale(user):
    return user.groups.filter(name='Direction Générale').exists()