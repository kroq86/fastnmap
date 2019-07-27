import subprocess

with open('ip.txt','w') as list: 
    sub = subprocess.run(['nmap', '192.168.1.'+'*'], stdout=list, text=True)


print(sub)
