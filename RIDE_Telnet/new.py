__author__ = 'teggenbe'

from N2x import N2x

paramDict = {"type": "tcl", "controller": "10.13.254.29", "session": "BBDLC_Data", "mode": "connect"}

#print paramDict
instance = N2x("C:/Tcl/bin", "path")
instance.n2xConnect(paramDict)
