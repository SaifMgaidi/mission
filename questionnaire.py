import json
import os
import sys

# Affiche les informations du questionnaire
def afficher_infos_du_questionnaire(infos):
    print()
    print("Catégorie:", infos[0][0])
    print("Titre:", infos[0][1])
    print("Difficulté:", infos[0][2])
    print("Nombres de Questions:", infos[0][3])
    print()

# Fonction qui vérifie l'existence du fichier
def fichier_exist(filename):
    if os.path.exists(filename):
        return True
    else:
        return False

# Fonction qui demande à l'utilisateur de rentrer le fichier Json à charger
def demande_du_fichier_json():
    filename = input('Nom du fichier Json: ')
    if fichier_exist(filename):
        return filename
    else:
        print('Erreur: le fichier Json est introuvable')
        return demande_du_fichier_json()
    
# Prend en paramètre le nom du fichier
# La fonction lit et récupère les données du fichier Json
def lecture_et_recuperation_donnees_json(filename):
    if not fichier_exist:
        print('Erreur: Le fichier est introuvable')
        return None
    f = open(filename, "r")
    data = json.load(f)
    f.close()
    return data



class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i][0])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))


        if self.choix[reponse_int-1][1]:
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions, infos):
        self.questions = questions
        self.infos = infos

    def lancer(self):
        score = 0
    
        print("Bienvenue !")
        print("Retrouve ci-dessous, les informations du Quizz !")

        afficher_infos_du_questionnaire(self.infos)
        
        print("A vous de jouer !")
        print()
        for i in range(0, len(self.questions)):
            print(f"question {i+1} / {len(self.questions)}")
            if self.questions[i].poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


# Pour ligne de commande: Teste si un paramètre est passé en entrée
if len(sys.argv) > 1:
    filename = sys.argv[1]
    # Vérifie le fichier passé en paramètre
    if fichier_exist(filename):
        pass
    else:
        print('Erreur: Le paramètre de la ligne de commande ne correspond à aucun fichier Json')
        exit()
else:
    filename = demande_du_fichier_json()


# Variable qui récupère les données du fichier Json
data = lecture_et_recuperation_donnees_json(filename)

# On ajoute les questions dans la liste questions
questions = []
for question in data["questions"]:
    titre = question["titre"]
    choix = question["choix"]
    questions.append(Question(titre, choix))

# On ajoute aussi les infos concernant le questionnaire
questionnaires_infos = [(data["categorie"], data["titre"], data["difficulte"], len(questions))]


# On passe la liste des questions (premier paramètre)
# On passe les informations du questionnaire (deuxième paramètre)
Questionnaire(questions, questionnaires_infos).lancer()