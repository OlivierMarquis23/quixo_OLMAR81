import api
import quixo


def main():
    args = quixo.interpréter_la_commande()
    idul = args.idul
    jeton = '0ef76153-d06c-4f36-82c5-6b35aba72f3c'

    try:
        id_partie, joueurs, etat = api.initialiser_partie(idul, jeton)

        while True:
            print(quixo.formater_le_jeu(joueurs, etat['plateau']))

            origine, direction = quixo.choisir_un_coup()

            try:
                id_partie, etat, _ = api.jouer_un_coup(id_partie, origine, direction, idul, jeton)
            except StopIteration as e:
                print(f"Le gagnant est: {e}")
                break
            except (PermissionError, RuntimeError, ConnectionError) as e:
                print(f"Erreur : {e}")

    except (PermissionError, RuntimeError, ConnectionError) as e:
        print(f"Erreur lors de l'initialisation de la partie : {e}")

if __name__ == "__main__":
    main()