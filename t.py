import os
import subprocess

print("hello")
string = 'git commit -m message'
string = 'git log'
cmd = string.split(' ')
try:
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    print(result)
except Exception as e:
    print(e)