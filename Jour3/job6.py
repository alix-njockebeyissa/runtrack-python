chaine = "abcdefghijklmnopqrstuvwxyz" * 10
n = len(chaine)
for i in range(1, n+1, 2):
    espace = (n-i)//2
    print(" "*espace + chaine[:i] + " "*espace)