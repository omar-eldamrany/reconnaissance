import subprocess,socket,json
from shodan import Shodan
print(subprocess.run("./bash.sh",shell=True))

#getting files ready
subfinder = open("subfinder.txt" , 'r')
sublister = open("sublister.txt" , "r")
reconng = open('results.csv' , "r")
reconng_ = open("recon-ng_.txt","w")
theharvester = open('theharvester.json')
ips = open("ips.txt","w")

#getting only the hosts from recon-ng file
for line in reconng:
    host = line.split(",")
    reconng_.write(host[0].replace('"',"")+"\n")

reconng_.close()
reconng_ = open("recon-ng_.txt","r")  

ip_list = []

myShodan = Shodan('7iMFmNtwrNRRX2XKfrSw4kGQ4TfwwKes')
kingfahd = myShodan.search("kfupm.edu.sa")
for match in kingfahd["matches"]:
    if isinstance(match,dict):
        for key,value in match.items():
            if match["ip_str"]:
                if match['ip_str'] in ip_list:
                    pass
                else:
                    ip_list.append(match['ip_str'])

#getting only the ips from theharvester file
data = json.load(theharvester)
for host in data["hosts"]:
    hostip = host.split(":")
    try:
        if hostip[1].find(",") == -1:
            if (hostip[1] not in ip_list):
                ip_list.append(hostip[1])
        else:
            x = hostip[1].split(",")
            for i in x:
                if (i not in ip_list):
                    ip_list.append(i.strip()) 
    except:
        continue 

#merging all hosts found from subfinder,sublister,recon-ng
hosts = subfinder.readlines() + sublister.readlines() + reconng_.readlines()
print(f'hosts: {len(hosts)}') #before
hosts = list(dict.fromkeys(hosts)) #deleting duplicates hosts
print(f'hosts after filtering duplicates: {len(hosts)}') #after 

#resolving ips from hosts subfinder,sublister,recon-ng
for host in hosts:
    the_host = host.strip() 
    try:
        ip = socket.gethostbyname(the_host)
        if (ip not in ip_list):
            ip_list.append(ip)     
    except:
        #   failed to get ip for {the_host}
        continue

#saving all ips found from subfinder,sublister,recon-ng,theharvester
#with no duplicates 
for an_ip in ip_list:
    ips.write(an_ip+"\n")

#getting only the emails from theharvester file
emailsfile = open("emails.txt" , "w")
emails = []
for email in data["emails"]:
    emails.append(email)
    emailsfile.write(email+"\n")

subfinder.close()
sublister.close()
reconng.close()
reconng_.close()
ips.close()
emailsfile.close()

print(f'emails found {len(emails)}')
print(f'unique ips found {sum(1 for line in open("ips.txt"))}')


ip_list = []

print(myShodan.info())



print(ip_list)                        

