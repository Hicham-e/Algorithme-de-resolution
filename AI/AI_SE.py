import tkinter as tk
from tkinter import messagebox

# Base de connaissances des symptômes et diagnostics
diagnostics = {
    "Symptom1": "Diagnosis 1",
    "Symptom2": "Diagnosis 2",
    "Symptom3": "Diagnosis 3",
}

# Fonction diagnostic
def diagnostic(symptom):
    if symptom in diagnostics:
        return diagnostics[symptom]
    return "No diagnosis found"

# Fonction de la soumission du formulaire
def submit():
    # Récupérer le symptôme de l'utilisateur
    user_symptom = entry_symptom.get()

    # diagnostic
    diagnosis = diagnostic(user_symptom)

    # Afficher le diagnostic
    messagebox.showinfo("Diagnosis", diagnosis)

    # Effacer le contenu de l'entrée
    entry_symptom.delete(0, tk.END)

# Créer une interface utilisateur simple avec Tkinter
root = tk.Tk()
root.title("Computer Malfunction Diagnosis")
root.geometry("400x200")  # Taille de la fenêtre (largeur x hauteur)

# Entrée du symptôme
label_symptom = tk.Label(root, text="Enter a symptom:")
label_symptom.pack()

entry_symptom = tk.Entry(root, width=30)  # Largeur du champ d'entrée
entry_symptom.pack()

# Bouton de soumission
submit_button = tk.Button(root, text="Diagnose", command=submit)
submit_button.pack()

root.mainloop()
