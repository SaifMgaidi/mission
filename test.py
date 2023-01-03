import unittest
from unittest.mock import patch
import questionnaire
import questionnaire_import
import os
import json

def additionner(a, b):
    return a+b

def multiplier(a, b):
    return a*b


def conversion_nombre():
    str_nb = input("Entrez Nombre: ")
    return int(str_nb)

"""class TestUnitaireDemp(unittest.TestCase):
    def test_conversion_nombre_valide(self):
        with patch("builtins.input", return_value="10"):
            self.assertEquals(conversion_nombre(), 10)
        with patch("builtins.input", return_value="15"):
            self.assertEquals(conversion_nombre(), 15)

    def test_conversion_nombre_invalide(self):
        with patch("builtins.input", return_value="fd"):
            self.assertRaises(ValueError, conversion_nombre)"""


class TestQuestion(unittest.TestCase):
    def test_question_bonne_ou_mauvaise_reponse(self):
        choix = ["choix1", "choix2", "choix3"]
        q = questionnaire.Question("test", choix, "choix2")
        with patch("builtins.input", return_value="1"):
            self.assertFalse(q.poser(1, 1))
        with patch("builtins.input", return_value="2"):
            self.assertTrue(q.poser(1, 1))
        with patch("builtins.input", return_value="3"):
            self.assertFalse(q.poser(1, 1))

class TestQuestionnaire(unittest.TestCase):
    def test_questionnaire_lancer_alien_debutant(self):
        filename = os.path.join("test_data", "cinema_alien_debutant.json")
        q = questionnaire.Questionnaire.from_file_json(filename)
        self.assertIsNotNone(q)
        self.assertEqual(q.nb_questions, 10)
        self.assertEqual(q.titre, "Alien")
        self.assertEqual(q.categorie, "Cinéma")
        self.assertEqual(q.difficulte, "débutant")
        with patch("builtins.input", return_value= "1"):
            self.assertEqual(q.lancer(), 1)

    def test_questionnaire_invalide(self):
        filename = os.path.join("test_data", "test_invalide_1.json")
        q = questionnaire.Questionnaire.from_file_json(filename)
        self.assertIsNotNone(q)

        filename = os.path.join("test_data", "test_invalide_2.json")
        q = questionnaire.Questionnaire.from_file_json(filename)
        self.assertIsNone(q)

        filename = os.path.join("test_data", "test_invalide_3.json")
        q = questionnaire.Questionnaire.from_file_json(filename)
        self.assertIsNone(q)
        

class TestQuestionnaireImport(unittest.TestCase):
    def test_import_format_json(self):
        questionnaire_import.generate_json_file("Animaux", "Les chats", "https://www.codeavecjonathan.com/res/mission/openquizzdb_50.json")

        filenames = ["animaux_leschats_debutant.json", "animaux_leschats_confirme.json", "animaux_leschats_expert.json"]    

        for filename in filenames:
            try:
                f = open(filename, "r")
                data_json = f.read()
                f.close()
                data = json.loads(data_json)
            except:
                self.fail("Erreur lors de la désérialisation des données json: " + filename)

            self.assertTrue(os.path.isfile(filename))

            self.assertIsNotNone(data.get("categorie"))
            self.assertIsNotNone(data.get("titre"))
            self.assertIsNotNone(data.get("difficulte"))
            self.assertIsNotNone(data.get("questions"))
            self.assertGreater(len(data.get("titre")), 0)
            self.assertGreater(len(data.get("questions")), 0)
            for question in data.get("questions"):
                self.assertIsNotNone(question.get("titre"))
                self.assertIsNotNone(question.get("choix"))
                self.assertGreater(len(question.get("titre")), 0)
                self.assertGreater(len(question.get("choix")), 0)        
                
                for choix in question.get("choix"):
                    self.assertGreater(len(choix[0]), 0)
                    self.assertTrue(isinstance(choix[1], bool))
                
                bonne_reponse = [i[0] for i in question.get("choix") if i[1]]
                self.assertEqual(len(bonne_reponse), 1)
                


unittest.main()