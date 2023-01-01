import json
import os

def demande_et_verification_du_fichier_json():
    filename = input("questionnaires json: ")
    if os.path.exists(filename):
        return filename
    else:
        print("Erreur: Le fichier est introuvable")
        return demande_et_verification_du_fichier_json()


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
        print("Catégorie:", self.infos[0][0])
        print("Titre:", self.infos[0][1])
        print("Difficulté:", self.infos[0][2])
        print("Nombres de Questions:", len(self.questions))
        print("A vous de jouer !")
        print()
        for i in range(0, len(self.questions)):
            print(f"question {i+1} / {len(self.questions)}")
            if self.questions[i].poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


# Le fichier json est demandé à l'utilisateur, puis il est verifié
filename = demande_et_verification_du_fichier_json()

f = open(filename, "r")
data = json.load(f)
f.close()

# On ajoute une question avec son titre et ses choix dans une liste qui regroupe toutes
# les questions du fichier json

questionnaires_infos = [(data["categorie"], data["titre"], data["difficulte"])]
questions = []

for question in data["questions"]:
    titre = question["titre"]
    choix = question["choix"]
    questions.append(Question(titre, choix))



# On ne crée plus de question en dur, on passe directement la liste qui contient toutes les questions
Questionnaire(questions, questionnaires_infos).lancer()