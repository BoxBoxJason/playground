from django.shortcuts import render,get_object_or_404,redirect
from taverne.models import Character,Equipement,checkMove
from taverne.forms import MoveForm


def taverne_view(request):
    clients = Character.objects.filter(id_character__isnull=False)
    activites = Equipement.objects.filter(id_equip__isnull=False)
    occupants = {}
    for activite in activites:
        tmp = Character.objects.filter(lieu__id_equip=activite.id_equip).first()
        if tmp is not None:
            occupants[activite.id_equip] = tmp.id_character
    return render(request, 'taverne/taverne.html', {'clients':clients,'activites':activites,'occupants':occupants},)


def client_detail(request, pk,msg=''):
    client = get_object_or_404(Character, id_character=pk)
    
    if request.method == 'POST':
        form = MoveForm(request.POST)
        if form.is_valid():
            ancien_lieu = get_object_or_404(Equipement, id_equip=client.lieu.id_equip)
            ancien_lieu.disponibilite = "Libre"
            
            ancien_lieu.save()
            form.save(commit=False)

            nouveau_lieu = form.cleaned_data['lieu']
            if nouveau_lieu.disponibilite != 'Occupé':
                client.etat, nouveau_lieu.disponibilite, msg = checkMove(nouveau_lieu.id_equip, client.etat,client.id_character)
                if not msg:
                    client.lieu = nouveau_lieu
                    nouveau_lieu.save()
                    client.save()

            else:
                msg = f"Le lieu {nouveau_lieu.id_equip}est occupé !"

            if msg != '':
                return render(request, 'taverne/client_detail.html', {'message':msg,'client':client})
            else:
                return redirect('taverne_view')
    else:
        form = MoveForm()

    return render(request, 'taverne/client_detail.html', {'client': client, 'form': form, 'message': ""})


def activite_detail(request,pk):
    activite = get_object_or_404(Equipement,pk=pk)
    occupant = None
    if activite.disponibilite != 'Libre':
        occupant = Character.objects.filter(lieu__id_equip=pk).first()
    return render(request, 'taverne/activite_detail.html', {'activite': activite,'occupant':occupant})
