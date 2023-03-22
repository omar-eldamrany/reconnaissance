#! /usr/bin/bash
echo "Searching using TheHarvester"
echo "------------------------"
theHarvester -d kfupm.edu.sa -b bing,yahoo -f theharvester
echo "Searching using Sublister"
echo "------------------------"
sublist3r -d kfupm.edu.sa -o sublister.txt
echo "Searching using dnsrecon"
echo "------------------------"
dnsrecon -d kfupm.edu.sa -c dnsrecon.txt
echo "Searching using subfinder" 
echo "------------------------"
docker run projectdiscovery/subfinder:latest -d kfupm.edu.sa >> subfinder.txt
echo "Searching using recon-ng"
echo "------------------------"
recon-cli -w kingfahd -m domains-hosts/bing_domain_web -o SOURCE=kfupm.edu.sa -x
recon-cli -w kingfahd -m reporting/csv -o SOURCE=kfupm.edu.sa -x
exit

