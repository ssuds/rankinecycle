# Rankine Cycle
# Shreyas Sudhakar
# 2018

from CoolProp.CoolProp import PropsSI
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Known Information about Rankine Cycle

# Pb = 80*10**10 #80 bar pressure at boiler THIS IS MOVED TO THE RANKINE FUNCTION

Tb = PropsSI("T", "P", Pb, "Q", 1, "Water") #We know that it is a saturated liquid leaving the boiler
Td = PropsSI("T", "P", Pd, "Q", 0, "Water") #We know that it is a saturated fluid leaving the turbine
Tc = Td #2 phase fluid through condenser, temperature doesnt change from state C to D

#Function to solve system

#two unknowns are temperature of the fluid leaving the pump and the quality of the water going into the condenser

#adding a for loop around this solver will allow us to perturb the turbine inlet pressure and see the sensitivity to it
def rankine(inputs, Pb=80*10**5): #adding an argument for Pb and specifying the default value
    qc, Te = inputs #using a parameter called inputs because the solvers are used to having all the inputs under one variable name
    #equations of state (4 states)
    Pc = 0.08 * 10 ** 5  # condenser pressure of 0.08 bar
    # assuming no pressure drop across boiler and condenser
    Pd = Pc
    Pa = Pb
    sb = PropsSI("S", "T", Tb, "Q", 1, "Water") #entropy at state b as a saturated liquid
    sc = PropsSI("S", "T", Tc, "Q", qc, "Water") #entropy at state c as a 2 phase fluid
    sd = PropsSI("S", "P", Pd, "Q", 0, "Water") #entropy at state d as a saturated liquid
    se = PropsSI("S", "P", Pe, "Te", Te, "Water") #entropy at state e as a compressed liquid

    eqns = [
        sb - sc, 
        sd - se
    ] #normally would have written that sb = sc, sd = se (isentropic processes), so these differences should equal zero. The idea is that the solver will try to find a zero (minimize this function)
    return eqns

qc, Te = fsolve(rankine, [0.8, 300])

states = [
    [Tb, Pb],
    [Tc, Pc],
    [Td, Pd],
    [Te, Pe]

]
    sb = PropsSI("S", "T", Tb, "Q", 1, "Water") #entropy at state b as a saturated liquid
    sc = PropsSI("S", "T", Tc, "Q", qc, "Water") #entropy at state c as a 2 phase fluid
    sd = PropsSI("S", "P", Pd, "Q", 0, "Water") #entropy at state d as a saturated liquid
    se = PropsSI("S", "P", Pe, "Te", Te, "Water") #entropy at state e as a compressed liquid

pressures = [Pb, Pc]
isobars = []  #gives us the two constant pressure lines
for pressure in pressures:
    isobar = []
    for entropy in range(0, 8000):
        isobar.append(PropsSI("T", "P", pressures, "S", entropy, "Water"))
        isobars.append(isobar)

#can repeat process for saturation line seen in thermoprop code
print(qc, Te)