import json
import sys


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def from_data_json(data):
        # Data["choix"] --> (choix(str), bool(bonne_réponse))
        choix = [i[0] for i in data["choix"]]
        bonne_reponse = [i[0] for i in data["choix"] if i[1]]
        # Retourne None si une question possède pas ou plusieurs bonne réponse
        if len(bonne_reponse) != 1:
            return None
        q = Question(data["titre"], choix, bonne_reponse[0])
        return q

    def poser(self, num_question, nb_questions):
        print(f"QUESTION {num_question} / {nb_questions} ")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
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
    def __init__(self, categorie, titre, questions, difficulte):
        self.categorie = categorie
        self.titre = titre
        self.questions = questions
        self.difficulte = difficulte

    def lancer(self):
        score = 0
        print("QUIZZ")
        print("----------")
        print("Catégorie:", self.categorie)
        print("Titre:", self.titre)
        print("Difficulté:", self.difficulte)
        print("Nombres de Question:", len(self.questions))
        print("----------")
        print()

        for i in range(len(self.questions)):
            if self.questions[i].poser(i+1, len(self.questions)):
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score

    def from_data_json(data):
        questions = [Question.from_data_json(question) for question in data["questions"]]
        # Récupère les questions qui n'ont pas d'anomalie (qui ne retourne pas None)
        questions = [question for question in questions if question]
        return Questionnaire(data["categorie"], data["titre"], questions, data["difficulte"]).lancer()


# Lancement du Questionnaire en ligne de commande
if len(sys.argv) < 2:
    print("Erreur: Aucun fichier JSON n'a été passé en entrée")
    exit()
else:
    filename = sys.argv[1]
    if not filename[-5:] == ".json":
        print("Erreur: Veuillez entrer un fichier JSON en entrée")
    else:

        f = open(filename, "r")
        data = f.read()
        f.close()
        data_json = json.loads(data)

        Questionnaire.from_data_json(data_json)