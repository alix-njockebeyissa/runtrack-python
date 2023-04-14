def proche_mot(mot):
    # Convertir le mot en une liste de caractères
    caracteres = list(mot)
    n = len(caracteres)
    for i in range(n-1, 0, -1):
        if caracteres[i] > caracteres[i-1]:
            j = i
            while j < n and caracteres[j] > caracteres[i-1]:
                j += 1
            j -= 1
            caracteres[i-1], caracteres[j] = caracteres[j], caracteres[i-1]
            caracteres[i:] = reversed(caracteres[i:])
            nouveau_mot = "".join(caracteres)
            return nouveau_mot
    
    return mot