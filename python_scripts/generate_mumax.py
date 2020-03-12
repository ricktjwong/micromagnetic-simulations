import math


def generate_script(x: str, y: str, z: str, s: str, i: int):
    lines = ''
    lines += 'OutputFormat = OVF1_TEXT\n'
    lines += 'MsPerm := 800e3\nExchangeEPerm := 13e-10\nAlphaPerm := 0.01\n'
    lines += 'MsCo := 1400e3\nExchangeECo := 30e-12\nAlphaCo := 0.015\n'
    lines += 'Ms := MsPerm\nExchangeE := ExchangeEPerm\nAlph := AlphaPerm\n'
    lines += 'x := ' + x + '\n'
    lines += 'y := ' + y + '\n'
    lines += 'z := ' + z + '\n'
    lines += 's := ' + s + '\n'
    lines += 'SetCellsize(5e-9, 5e-9, 5e-9)\n'
    Nx = math.ceil((float(x) * 8 + float(s) * 7) / 5e-9)
    Ny = math.ceil((float(y) + 400e-9) / 5e-9)
    Nz = math.ceil(float(z) / 5e-9)
    lines += 'SetGridsize(' + str(Nx) + ', ' + str(Ny) + ', ' + str(Nz) + ')\n'
    with open('8array.' + str(i) + '.mx3', 'w') as f1:
        for line in lines:
            f1.write(line)
        with open('8array_rect_boilerplate.mx3') as f:
            for line in f:
                f1.write(line)


sweep_width = [i for i in range(20, 210, 10)]
for i in range(len(sweep_width)):
    generate_script(x=str(sweep_width[i]) + 'e-9',
                    y='600e-9',
                    z=str(sweep_width[i]) + 'e-9',
                    s='20e-9',
                    i=i)
