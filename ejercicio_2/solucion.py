def calcular_campeones(prix_pilots, placements, n_systems, scoring_systems):
    """
    Funcion que calcula los campeones de un prix de acuerdo a la manera de calcular el puntaje
        Args:
            prix_pilost: un array con el numero de carreras del prix y el número de pilotos
            placements: un array de array con el posicionamiento de los pilotos en las carreras del prix
            n_systems: numero de sistemas a utilizar
            scoring_systems: Valor de las posiciones, donde el primer elemento es el cual se le asiganara
            el nuemroK que representa cual es la ultima posición a la cual se le dara puntaje
        Return:
            Un array con la posición de los campeones de acuerdo al sistema de puntaje
            también los imprime            
    """
    champions = []
    for scoring_system in scoring_systems:
        # Initialize a dictionary to store points for each pilot
        pilot_points = {pilot: 0 for pilot in range(1, prix_pilots[1] + 1)}
        K = scoring_system[0]
        points = scoring_system[1:]

        # Calculate points for each pilot in each race
        for placement in placements:
            for i, pilot in enumerate(placement):
                if i < K:  # Give points only if the pilot finished within the scoring positions
                    pilot_points[pilot] += points[i]

        # Find pilots with the highest points
        max_points = max(pilot_points.values())
        champions_for_system = [pilot for pilot, points in pilot_points.items() if points == max_points]

        # Format output string for champions
        champions_string = " ".join(map(str, champions_for_system))
        champions.append(champions_string)
    
    for champion in champions:
        print(champion)
    return champions
