def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note % 5 >= 3 and note >= 38:
            note_arrondie = note + (5 - note % 5)
            notes_arrondies.append(note_arrondie)
        else: 
            notes_arrondies.append(note)
    return notes_arrondies