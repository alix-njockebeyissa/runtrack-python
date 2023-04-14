def chiffrement_cesar(message, k):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            nouvelle_pos = ord(lettre.lower()) - ord('a') + k
            if nouvelle_pos > 25:
                nouvelle_pos -= 26
            elif nouvelle_pos < 0:
                nouvelle_pos += 26
            lettre_chiffree = chr(nouvelle_pos + ord('a'))
            message_chiffre += lettre_chiffree.upper() if lettre.isupper() else lettre_chiffree.lower()
        else:
            message_chiffre += lettre
    return message_chiffre