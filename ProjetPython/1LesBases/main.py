# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')



# # print("Bonjour je suis cody24")
# # nom = input("Quel est ton prénom ? ")
# age = int(input("Quel est ton age ? "))
# # print("Bonjour " + nom + ", tu as " + str(age) + " ans")
# # print("Bonjour" , nom, "Tu as", age, "ans")

# # if age >= 18:
# #     print("Tu es majeur")
# # else:
# #     print("Tu es mineur")

# if age < 12:
#     print("Tu es encore un enfant 👶")
# elif age < 18:
#     print("Tu es un ado 🎮")
# else:
#     print("Tu es un adulte 💼")

# # Les boucles ****
# print("Bonjour")
# print("Bonjour")
# print("Bonjour")



# for i in range(3):
#     print("Bonjour")









# # **************************Exercices************************

# # ***Correction quizz Défi n°3***

# print("Bienvenue dans le Quiz de Cody 🤖")

# # Question 1
# reponse1 = input("Quelle est la capitale de la France ? ")
# if reponse1.lower() == "paris":   # .lower() rend la comparaison insensible à la casse
#     print("✅ Bravo, réponse est correct !")
# else:
#     print("❌ Dommage , la réponse est fausse! La capitale est Paris.")

# # Question 2
# reponse2 = input("Combien font 2 + 2 ? ")
# if reponse2 == "4":   # pas besoin d'int ici car on compare à une chaîne
#     print("✅ Bravo, la réponse est correct ! !")
# else:
#     print("❌ Dommage , la réponse est fausse ! La réponse est 4.")

# # Question 3
# reponse3 = input("Python est un serpent ou un langage ? ")
# if reponse3.lower() == "langage":
#     print("✅ Bravo, la réponse est correct !")
# else:
#     print("❌ Dommage , la réponse est fausse, Python est un langage de programmation.")




# # ***Correction quizz Défi n°3+***

# print("Bienvenue dans le Quiz de Cody 🤖")

# # Initialisation du score
# score = 0

# # Question 1
# reponse1 = input("Quelle est la capitale de la France ? ")
# if reponse1.lower() == "paris":   # .lower() rend la comparaison insensible à la casse
#     print("✅ Bravo, la réponse est correcte !")
#     score += 1
# else:
#     print("❌ Dommage, la réponse est fausse ! La capitale est Paris.")

# # Question 2
# reponse2 = input("Combien font 2 + 2 ? ")
# if reponse2 == "4":   # pas besoin d'int ici car on compare à une chaîne
#     print("✅ Bravo, la réponse est correcte !")
#     score += 1
# else:
#     print("❌ Dommage, la réponse est fausse ! La réponse est 4.")

# # Question 3
# reponse3 = input("Python est un serpent ou un langage ? ")
# if reponse3.lower() == "langage":
#     print("✅ Bravo, la réponse est correcte !")
#     score += 1
# else:
#     print("❌ Dommage, la réponse est fausse, Python est un langage de programmation.")

# # Affichage du score final
# print("🎯 Ton score final est :", score, "/ 3")

