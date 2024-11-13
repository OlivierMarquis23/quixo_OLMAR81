import requests

def initialiser_partie(idul, jeton):
    URL = 'https://pax.ulaval.ca/quixo/api/a24/partie/'
    response = requests.post(URL, auth=(idul, jeton))
    
    if response.status_code == 200:
        data = response.json()
        print("Réponse du serveur :", data)
        id_partie = data.get('id')
        etat = data.get('état')
        joueurs = etat.get('joueurs')
        if not joueurs:
            raise ValueError("Les joueurs n'ont pas été récupérés correctement.")
        return (id_partie, joueurs, etat)
    
    elif response.status_code == 401:
        message = response.json().get('message')
        raise PermissionError(message)
    
    elif response.status_code == 406:
        message = response.json().get('message')
        raise RuntimeError(message)
    
    else:
        raise ConnectionError()