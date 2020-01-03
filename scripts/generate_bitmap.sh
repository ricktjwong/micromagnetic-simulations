#!/bin/bash

tclsh /Users/ricktjwong/oommf/oommf.tcl avf2ppm -format B24 -config ../avf2ppm.config ../cobalt-halbach-2rows/halbach2rows.0.out/m000000.ovf
tclsh /Users/ricktjwong/oommf/oommf.tcl avf2ppm -format B24 -config ../avf2ppm.config ../cobalt-halbach-2rows/halbach2rows.0.out/m000001.ovf