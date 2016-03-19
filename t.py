import os
import subprocess

print("hello")
string = "git status"
cmd = string.split(' ')
try:
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    print(result)
except Exception as e:
    print(e)