# oommf-simulations
Configuration files for OOMMF

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
