import os
import subprocess

def splitCommand(cmd):
    cmd = cmd.lstrip().rstrip()
    
    scmd = cmd.split(' ')
    
    message = ''
    quoteType = ''
    nscmd = []
    
    for value in scmd:
        if value == '':
            continue
        if quoteType == '':
            if value[0] == '"':
                quoteType = '"'
                message = message + value + ' '
            elif value[0] == "'":
                quoteType = "'"
                message = message + value + ' '
            else:
                nscmd.append(value)
        else:
            message = message + value + ' '
    if message != '':
        nscmd.append(message)
        
    return nscmd                
        
    



print("hello")
string = 'git commit  -m "heelo wolrd'
#string = 'git status'

#cmd = string.split(' ')
#try:
com = ''
for value in splitCommand(string):
    print(value)
    com = com + value
print com
        
        
    #result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    #print(result)
#except subprocess.CalledProcessError as e:
#    print(e.output)
#except Exception as e:
#    print(e)