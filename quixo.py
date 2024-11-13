def formater_entête(joueurs):
    """
    Formate la légende des joueurs en art ASCII.

    Args:
        joueurs (list): Liste de deux noms de joueurs.

    Returns:
        str: Légende formatée en art ASCII.
    """
    return f"Légende:\n   X={joueurs[0]}\n   O={joueurs[1]}"

def formater_le_damier(plateau):
    """
    Formate le plateau de jeu en art ASCII.

    Args:
        plateau (list): État actuel du plateau de jeu.

    Returns:
        str: Plateau formaté en art ASCII.
    """
    lignes = []
    for i, ligne in enumerate(plateau):
        lignes.append(f"{i+1} | {' | '.join(ligne)} |")
        if i < 4:
            lignes.append("  |---|---|---|---|---|")

    damier = (
        "   -------------------\n" +
        "\n".join(lignes) +
        "\n--|---|---|---|---|---|\n" +
        "  | 1   2   3   4   5 |"
    )
    return damier