from django.db import models

class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id_equip)


class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    titre = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id_character)


lieuxEtat = {
    'Toilettes':('Ivre','Sobre'),
    'Bras de fer':('Euphorique','Assoiffé'),
    'Poker':('Sobre','Euphorique'),
    'Table':('Assoiffé','Ivre')
}

def checkMove(nouveau_lieu,etat,nom_client):
    nouvel_etat = etat
    msg = ""
    if lieuxEtat[nouveau_lieu][0] == etat:
        nouvel_etat = lieuxEtat[nouveau_lieu][1]
    else:
        msg = f"{nom_client} n'est pas en état de faire ça ! ({etat} != {lieuxEtat[nouveau_lieu][0]})"

    disponibilite = "Occupé"
    if nouveau_lieu == 'Toilettes':
        disponibilite = 'Libre'
    return nouvel_etat,disponibilite,msg
