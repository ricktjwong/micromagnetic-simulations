import os
import math


def round_ten(x: int) -> int:
    return int(math.ceil(x / 10.0)) * 10


def generate_single_magnet(x: str, y: str, z: str, i: int):
    lines = ''
    lines += 'OutputFormat = OVF1_TEXT\n'
    lines += 'MsPerm := 800e3\nExchangeEPerm := 13e-12\nAlphaPerm := 0.01\n'
    lines += 'MsCo := 1400e3\nExchangeECo := 30e-12\nAlphaCo := 0.015\n'
    lines += 'Ms := MsPerm\nExchangeE := ExchangeEPerm\nAlph := AlphaPerm\n'
    lines += 'x := ' + x + '\n'
    lines += 'y := ' + y + '\n'
    lines += 'z := ' + z + '\n'
    Nx = round_ten(float(x) / 5e-9)
    Ny = round_ten((float(y) + 400e-9) / 5e-9)
    Nz = math.ceil(float(z) / 5e-9)
    lines += 'SetCellsize(5e-9, 5e-9, 5e-9)\n'
    lines += 'SetGridsize(' + str(Nx) + ', ' + str(Ny) + ', ' + str(Nz) + ')\n'
    with open('perm_single.' + str(i) + '.mx3', 'w') as f1:
        for line in lines:
            f1.write(line)
        with open('single_boilerplate.mx3') as f:
            for line in f:
                f1.write(line)


def generate_parallel_magnets(x: str, y: str, z: str, s: str, i: int):
    lines = ''
    lines += 'OutputFormat = OVF1_TEXT\n'
    lines += 'MsPerm := 800e3\nExchangeEPerm := 13e-12\nAlphaPerm := 0.01\n'
    lines += 'MsCo := 1400e3\nExchangeECo := 30e-12\nAlphaCo := 0.015\n'
    lines += 'Ms := MsPerm\nExchangeE := ExchangeEPerm\nAlph := AlphaPerm\n'
    lines += 'x := ' + x + '\n'
    lines += 'y := ' + y + '\n'
    lines += 'z := ' + z + '\n'
    lines += 's := ' + s + '\n'
    lines += 'SetCellsize(5e-9, 5e-9, 5e-9)\n'
    Nx = round_ten((float(x) * 8 + float(s) * 7) / 5e-9)
    Ny = round_ten((float(y) + 400e-9) / 5e-9)
    Nz = math.ceil(float(z) / 5e-9)
    lines += 'SetGridsize(' + str(Nx) + ', ' + str(Ny) + ', ' + str(Nz) + ')\n'
    with open('sweep_width_sep_' + str(math.ceil(float(s)/1e-9)) +
              '/8array.' + str(i) + '.mx3', 'w') as f1:
        for line in lines:
            f1.write(line)
        with open('8array_rect_boilerplate.mx3') as f:
            for line in f:
                f1.write(line)


def generate_halbach_arrays(h_length: str, v_width: str, i: int):
    xsep = 100e-9
    lines = ''
    lines += 'OutputFormat = OVF1_TEXT\n'
    lines += 'L := 600e-9\n'
    lines += 'thickness_L := 100e-9\n'
    lines += 'thickness_S := 100e-9\n'
    lines += 'Nbars := 3\n'
    lines += 'w2 := L / (2*Nbars - 1)\n'
    lines += 'xsep := 100e-9\nysep := w2\n'
    lines += 'L2 := ' + h_length + '\n'
    lines += 'w1 := ' + v_width + '\n'
    lines += 'disp_n1 := xsep/2 + w1/2\n'
    lines += 'disp_n2 := 1.5*xsep + w1 + L2/2\n'
    lines += 'disp1 := xsep/2 + L2/2\n'
    lines += 'disp2 := 1.5*xsep + L2 + w1/2\n'
    Nx = math.ceil((4*xsep + 2*float(v_width) + 2*float(h_length)) / 5e-9)
    lines += 'SetPBC(2, 0, 0)\n'
    lines += 'SetGridsize(' + str(Nx) + ', 200, 30)\n'
    lines += 'SetCellsize(5e-9, 5e-9, 5e-9)\n'
    with open('halbach_vwidth_' + str(math.ceil(float(v_width)/1e-9)) +
              '/halbach_sweep.' + str(i) + '.mx3', 'w') as f1:
        for line in lines:
            f1.write(line)
        with open('halbach_sweep_boilerplate.mx3') as f:
            for line in f:
                f1.write(line)


# sweep_sep = [i for i in range(20, 110, 10)]
# sweep_width = [i for i in range(20, 620, 20)]
# for j in range(len(sweep_sep)):
#     if not os.path.exists('sweep_width_sep_' + str(sweep_sep[j])):
#         os.makedirs('sweep_width_sep_' + str(sweep_sep[j]))
#     for i in range(len(sweep_width)):
#         generate_parallel_magnets(x=str(sweep_width[i]) + 'e-9',
#                                   y='600e-9',
#                                   z='20e-9',
#                                   s=str(sweep_sep[j]) + 'e-9',
#                                   i=i)


# sweep_vwidth = [i for i in range(40, 220, 20)]
# sweep_hlength = [i for i in range(240, 620, 20)]
# for j in range(len(sweep_vwidth)):
#     if not os.path.exists('halbach_vwidth_' + str(sweep_vwidth[j])):
#         os.makedirs('halbach_vwidth_' + str(sweep_vwidth[j]))
#     for i in range(len(sweep_hlength)):
#         generate_halbach_arrays(h_length=str(sweep_hlength[i]) + 'e-9',
#                                 v_width=str(sweep_vwidth[j]) + 'e-9',
#                                 i=i)


x = [i for i in range(10, 610, 10)]
for i in range(len(x)):
    generate_single_magnet(x='100e-9',
                           y='600e-9',
                           z=str(x[i])+'e-9',
                           i=i)
