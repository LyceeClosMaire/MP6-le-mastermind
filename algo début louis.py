n = 4


c = []
for j in range(n):
    choix = input("choisir la couleur pour la case (choix)" + str(j))
    c.append(choix)
print(c)


reponses = []
for i in range(n):
    reponse = input("choisir la couleur pour la case (reponse)" + str(i))
    reponses.append(reponse)
print(reponses)


if reponses[0] == c[0]:
    print('le ', reponses[0], 'est a la bonne placer')
elif reponses