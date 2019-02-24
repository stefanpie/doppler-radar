import subprocess
import sys
import glob
path = '.'
filenames = glob.glob(path + '/in/*')
for filename in filenames:
	subprocess.call(["java", "-classpath", "toolsUI-4.6.11.jar", "ucar.nc2.FileWriter", "-in", filename, "-out", filename + ".nc"])
	subprocess.call(["rm", filename + ".uncompress"])
	subprocess.call(["mv", filename + ".nc", "./out"])