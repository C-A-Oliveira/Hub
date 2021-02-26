import os
import platform
import io
import re
import shutil

if platform.system() == "Windows":
    HOST_PATH = "C:/Windows/System32/drivers/etc/"
elif platform.system() == "Linux":
    HOST_PATH = "/etc/"
curr_hosts = open(HOST_PATH+"hosts")

#os.system("new_one.bat")
host_list = []
bkups = []
curr_bkup = 0
for dns in curr_hosts:
    if re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) ([a-z]*.)*", dns):
        host_list.append(dns.split())
        
if ['127.100.10.1', 'jtt.webapp']  in host_list or ['127.100.20.1', 'stuff.webapp']  in host_list:
    print("> Hosts Located! Ready to start servers")
    exit()
else:        
    print("> Hosts not listed!")
    '''
    The section will search for any previous backups created by this scrip. It keeps adding +1 to the number at the end
    '''
    for file in os.listdir(HOST_PATH):
        if file.endswith(".txt") and re.match(r"backup.hosts", file):
            bkups.append(os.path.join(HOST_PATH, file))
    if bkups != []:
        sorted(bkups)
        oldest = bkups.pop()
        curr_bkup = int(re.findall(r'\d+', oldest).pop()) ## DO NOT QUESTION MY DECISIONS PLS ;-;

    print('> Creating hosts backup as "backup.hosts{}.txt"'.format(str(curr_bkup+1).zfill(4)))    
    copy = os.path.join(HOST_PATH, "backup.hosts{}.txt".format(str(curr_bkup+1).zfill(4)))
    original = os.path.join(HOST_PATH, "hosts")
    shutil.copyfile(original, copy)

    
    '''
    Adding the hosts and dns' needed for this application to function 
    '''
    print("> Adding to host files")
    host_list.append(['127.100.10.1', 'jtt.webapp'])
    host_list.append(['127.100.20.1', 'stuff.webapp'])

    new_host = open(HOST_PATH+"hosts", 'w', encoding=curr_hosts.encoding)
    curr_hosts.close()
    for host in host_list:
         new_host.writelines("{} {}\n".format(host[0], host[1]))
    new_host.close()

