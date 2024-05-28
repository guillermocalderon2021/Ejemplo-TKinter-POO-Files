import sys
import os


import sys
 
sys.path.insert(0, 'c:/Users/GuillermoCalderón/Dropbox/Docencia/01 2024/PDC/EjemploPOO/logica')

from discografia import Discografia


mi_discografia=Discografia()
print(mi_discografia.buscar_codigo("DIS089"))