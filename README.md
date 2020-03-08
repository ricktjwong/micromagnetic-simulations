# micromagnetic-simulations
Scripts to process OOMMF vector files (.ovf)
Configuration files for OOMMF and mumax

## Utilities

### plot_quiver.py

Methods
1. plot_2D_quiver
    - Takes three arguments: (file_path: str, mag_dir: str, zslice: int)
    - Takes an ovf file (OOMMF format) and parses the xnodes, ynodes, znodes as well as the x, y and z step sizes. These are required to construct the mesh
    - mag_dir takes in a string of either 'x', 'y', 'z' or 'total', and specifies what to display for the magnitude of the contour line
    - zslice represent which slice of z you'd want to visualise
    - The units of the data corresponds to the setting in the OOMMF file

### plot_strayfield.py


## Installation of OOMMF

### Linux
<pre>
# Download essentials
$ sudo apt-get install build-essential

# Download OOMMF binary from website
$ wget https://math.nist.gov/oommf/dist/oommf20a2_20190930.tar.gz
$ gunzip -c oommf20a2_20190930.tar.gz | tar xvf -

# Download tcl
$ sudo apt-get install tcl
# Download extra tcl/tk components
$ sudo apt-get install tcl8.6-dev
$ sudo apt-get install tk8.6-dev

# Check if installation went okay
$ cd ./oommf && tclsh oommf.tcl +platform

# Build oommf
$ tclsh oommf.tcl pimake upgrade
$ tclsh oommf.tcl pimake distclean
$ tclsh oommf.tcl pimake
</pre>

### Running mif files using CLI
<pre>
$ tclsh oommf.tcl boxsi <PATH_TO_MIF_FILE>
</pre>
