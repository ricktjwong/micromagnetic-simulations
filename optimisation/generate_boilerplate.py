def generate_mumax_boilerplate(x: int, y: int) -> str:
    """
    Specify the x and y dimensions for gridspace
    The gridspace is 10nm for each cell
    Mumax cellsize is 5nm by default
    Currently only works for even x even spaces
    """
    lines = ''
    lines += generate_header(x, y)
    lines += generate_gridspace(x, y)
    lines += initialise_magnetisation(x, y)
    with open('boilerplate' + str(x) + 'x' + str(y) + '.mx3', 'w') as f:
        for line in lines:
            f.write(line)


def generate_header(x: int, y: int) -> str:
    lines = ''
    lines += 'OutputFormat = OVF1_TEXT\n'
    lines += 'nx := ' + str(x*2) + '\n'
    lines += 'ny := ' + str(y*2) + '\n'
    lines += 'nz := 2\n'
    lines += 'CellSize := 5e-9\n'
    lines += 'Translate := 5e-9\n'
    lines += 'GridSize := 10e-9\n'
    lines += 'SetGridsize(nx, ny, nz)\n'
    lines += 'SetCellsize(CellSize, CellSize, CellSize)\n'
    lines += 'Ms := 1400e3\n'
    lines += 'ExchangeE := 30e-12\n'
    lines += 'Alph := 0.015\n'
    return lines


def generate_gridspace(x: int, y: int) -> str:
    gridspace = []
    for i in range(int(x/2)):
        for j in range(int(y/2)):
            gridspace += [', Cuboid(GridSize, GridSize, GridSize)' +
                          '.transl(' + 'Translate*' + str(1 + 2*i) +
                          ', Translate*' + str(1 + 2*j) + ', 0))\n']
    gridspace += list(map(lambda x:
                      x.replace('Translate', '-Translate', 1), gridspace))
    gridspace += list(map(lambda x:
                      '-Translate'.join(x.rsplit('Translate', 1)), gridspace))
    gridspace = ['DefRegion(' + str(i+1) + x for i, x in enumerate(gridspace)]
    lines = ''.join(gridspace)
    return lines


def initialise_magnetisation(x: int, y: int) -> str:
    lines = ''
    lines += 'Msat.SetRegion(0, 0)\n'
    lines += 'm.SetRegion(0, uniform(0, 0, 0))\n'
    lines += 'Aex.SetRegion(0, 0)\n'
    lines += 'Kc1.SetRegion(0, 0)\n'
    empty_space = [i for i in range(1, x*y + 1, int(y/2))]
    for i in range(1, x*y + 1):
        if i in empty_space:
            lines += 'm.SetRegion(' + str(i) + ', uniform(0, 0, 0))\n'
            lines += 'Msat.SetRegion(' + str(i) + ', 0)\n'
            lines += 'Aex.SetRegion(' + str(i) + ', 0)\n'
            lines += 'Kc1.SetRegion(' + str(i) + ', 0)\n'
        else:
            lines += 'Msat.SetRegion(' + str(i) + ', Ms)\n'
            lines += 'Aex.SetRegion(' + str(i) + ', ExchangeE)\n'
            lines += 'Ku1.SetRegion(' + str(i) + ', 0)\n'
            lines += 'alpha.SetRegion(' + str(i) + ', Alph)\n'
    return lines


print(generate_mumax_boilerplate(16, 16))
