import re
def mot_de_passe(code):
    if len(code) < 8:
        return "Le code doit avoir au moins 8 caractères."
    
    if not re.search(r"\d", code ):
        return "le code doit avoir un chiffres au minimum"
    
    if not re.search(r"[A-Z]", code):
        return "le code doit avoir une majuscule"   
    
    if not re.search(r"[a-z]", code):
        return "le code doit avoir une minuscule"
    
    if not re.search(r"[&~#{}'()-^=@+]"):
        return "le code doit avoir un caractères"
    
    
    return "le code est correct"
    
code = input("Entrez votre mot de passe :")
resultat = mot_de_passe(code)
print(resultat)

