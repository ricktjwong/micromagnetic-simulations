import os


def initialise_gridspace(x: int, y: int):
    with open('./optimise.mx3') as f:
        with open('out.mx3', 'w') as f1:
            for line in f:
                f1.write(line)
            f1.write('endfile')


# Initialise gridspace of (x, y) = (2, 6) with random magnetisation directions
initialise_gridspace(2, 6)
