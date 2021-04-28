import sys
import time
import os
import glob
import numpy as np
import getpass
import subprocess

# Change obj_name accordingly
obj_name = 'Cuyo'
# Change dir name to folder containing out_periods_ObjName
dir = 'Cuyo_Abbie/test/'


os.system('cat %sout_periods_%s_* | sort -k1 > %sout_periods_%s'%(dir, obj_name,dir,obj_name)) 
