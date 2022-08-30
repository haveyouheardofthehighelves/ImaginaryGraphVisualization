import subprocess
import sys
import _thread
print(str(sys.argv))

subprocess.Popen(["python", "GraphInstances.py", str(sys.argv[1])])


