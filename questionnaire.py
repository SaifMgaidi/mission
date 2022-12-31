import json

# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#


# Modification de la Class Question (suppression de la variable bonne réponse)
# La Vérification de la bonne réponse se trouve dans le 2eme index des diffèrents choix

class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print("QUESTION")
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
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score



# Test de 1 question d'un fichier json

f = open("animaux_leschats_debutant.json", "r")
data = json.load(f)
f.close()

titre = data["questions"][0]["titre"]
choix = data["questions"][0]["choix"]



Questionnaire(
    (
    Question(titre, choix),
    )
).lancer()