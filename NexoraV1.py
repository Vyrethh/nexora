print(r""" ╔═══════════════════════════════════════════════════╗
║███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ║
║████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗║
║██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝███████║║
║██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██║║
║██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║║
║╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝║
╚═══════════════════════════════════════════════════╝
""")

print("                         Nexora")
print("                    DNS Scanner Toolkit")
print("                     Author: Vyreth")

start = input("Start DNS Scan? Y/N: ")
if start.lower() != 'y':
    print("Exiting...")

import dns
import dns.resolver
import socket



# This function tries to find a website name from an IP address.
def ReverseDNS(ip):
    try:
        # Try to look up the name of the website from the IP address
        result = socket.gethostbyaddr(ip)
    except:
        # If it doesn't work, just return an empty list
        return []
    # If it works, return a list with the main name and any extra names
    return [result[0]] + result[1]

# This function tries to find the IP address of a website or subdomain
def DNSRequest(domain):
    try:
        # Ask the DNS system for the IP address of the domain
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)  # Print the IP address we got
                print(f"Domain names: {ReverseDNS(answer.to_text())}")  # Try to get the name from the IP
    # If the domain doesn't exist or takes too long to answer, skip it
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout dns.resolver.NoAnswer):
        pass  # Do nothing if there's an error

# This function checks if common subdomains (like www, mail, etc.) exist for a website
def SubdomainSearch(domain, dictionary, nums):
    for word in dictionary:
        # Make a subdomain like www.google.com or mail.google.com
        subdomain = word + "." + domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0, 10):
                # Try adding numbers too, like www1.google.com, www2.google.com
                s = word + str(i) + "." + domain
                DNSRequest(s)

# --- Start of the program ---

# The main website you want to scan
domain = "google.com"

# This file should contain a list of words like 'www', 'mail', etc.
d = "subdomains.txt"
dictionary = []

# Read each word from the file and make a list
with open(d, "r") as f:
    dictionary = f.read().splitlines()

# Start looking for subdomains using the words from the file
SubdomainSearch(domain, dictionary, True)

# Nexora DNS Scanner - Feature Roadmap



# ✅ GOALS



# Stealth Mode

# - Low timeouts, silent mode, optional randomness

# - Suppress output unless flagged

# - (Future) Spoof source info


# Menu System

# - [0] Start scan

# - [1] Configure target

# - [2] Toggle stealth

# - [3] Exit


# Command-Line Options

# - Example: python nexora.py -s -d domain.com -r 8.8.8.8

# - Flags:

#   # -s = stealth mode

#   # -d = domain

#   # -r = DNS resolver


# Inputs

# - Let user decide domain

# - Let user pick DNS server

# - Toggle stealth


# Wordlist

# - Upgrade subdomains.txt (500–1000+)

# - Add support for –wordlist file


# GitHub Setup

# - Repo includes subdomains.txt

# - Tool looks for wordlist locally

# - Add requirements.txt for pip install


# Optional Upgrades

# - Export to file or JSON

# - Colors / formatting

# - ASCII logo

# - Threading for speed


# Recommended Layout

# Nexora/

# ├── nexora.py

# ├── subdomains.txt

# ├── README.md

# └── requirements.txt
