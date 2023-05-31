import os
from sys import platform
from yaspin import yaspin
import requests
from bs4 import BeautifulSoup

os.system("clear")
print("Operating System: ", platform)
print("\n\nWelcome to Leo's MC Server Creator! :3\n\nWhat kind of server do you want to create?\n\n1. Vanilla/Pure Server (Offical Server Images With No Plguins)\n2. Spigot Server (Has Plugins)\n3. Bukkit Server(Has Plugins)\n4. PaperMC Servers (Has Plugins, also compatible with Bukkit/Spigot Plugins)\n5. Forge Server (Mods and Such from Forge)\n\n")
serverkind = input("Input Your Choice Here and Press Enter >>> ")
if serverkind == "1":
    os.system("clear")
    print("Vanilla/Pure Server Creator:\n\n1. Install\n2. Repair/Reinstall\n\n")
    actionchoice = input(">>> ")
elif serverkind == "2":
    os.system("clear")
    
    try:
        url = "https://getbukkit.org/download/spigot"
            
        # Fetch raw HTML content
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
            
        #Get All Occurences Of 'h2' Tag, which is versions tag
        listallver = []
        texts = soup.find_all('h2')
        for text in texts:
            allvers = str(text.get_text())
            listallver.append(allvers)
    except:
        url = "https://getbukkit.org/download/spigot"
            
        # Fetch raw HTML content
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
            
        #Get All Occurences Of 'h2' Tag, which is versions tag
        listallver = []
        texts = soup.find_all('h2')
        for text in texts:
            allvers = str(text.get_text())
            listallver.append(allvers)
    
    print("Spigot Server Creator:\n\n1. Install\n2. Repair/Reinstall\n\n")
    actionchoice = input(">>> ")
    if actionchoice == "1":
        os.system("clear")
        print("Enter Your Preferred Spigot Version:\n\nVaild Spigot Versions are:\n",listallver,"\n\nPlease Enter The Version Number Without Spaces! e.g '1.17.4' not '1.17.4 '\n\n")
        ver = input(">>> ")
        ns_ver = ver.strip(" ")
        print(ns_ver)
        
        if ns_ver in listallver:
            print("Downloading Your Chosen Version of Spigot (",ns_ver, ") ...\n\n")
            with yaspin().moon as sp:
                sp.text = "Creating Directory..."
                try:
                    os.system("mkdir ~/Desktop/SPIGOTMCSERVER/")
                    if os.system("mkdir ~/Desktop/SPIGOTMCSERVER/") != 0:
                        raise Exception()
                    sp.ok("✅ ")
                except:
                    sp.fail("💥 ")  
                    
                sp.text = "Downloading..."
                try:
                    os.system("curl https://download.getbukkit.org/spigot/spigot-1.19.4.jar --output ~/Desktop/SPIGOTMCSERVER/spigot.jar -s")
                    sp.ok("✅ ")
                except:
                    sp.fail("❌ ")        
            print("\n\n\n Do you have a JDK Runtime above or equal to 17?\n\n1. Yes\n2. No\n\n(NEEDED BECAUSE AFTER MINECRAFT VERSION 1.18 THE JDK RUNTIME MUST BE ABOVE 17 AS WELL.)\n\n")
            javachoice = input(">>> ")
            if javachoice == "1":
                pass
            elif javachoice == "2":
                print("Downloadng JDK 18...")
                with yaspin().moon as sp:
                    sp.text = "Loading..."
                    try:
                        os.system("curl https://download.oracle.com/java/18/archive/jdk-18.0.2.1_macos-aarch64_bin.tar.gz --output ~/Desktop/SPIGOTMCSERVER/jdk.zip")
                        sp.ok("✅ ")
                    except:
                        sp.fail("❌ ")
                        
            os.system("cd ~/Desktop/SPIGOTMC")
            os.system("unzip jdk.zip")       
        else:
            print("Your Current Chosen Version: ", ns_ver, " Does not match the current list of available versions:\n\n", listallver)
            
elif serverkind == "3":
    os.system("clear")
    print("Bukkit Server Creator:\n\n1. Install\n2. Repair/Reinstall\n\n")
    actionchoice = input(">>> ")
elif serverkind == "4":
    os.system("clear")
    print("PaperMC Server Creator:\n\n1. Install\n2. Repair/Reinstall\n\n")
    actionchoice = input(">>> ")
elif serverkind == "5":
    os.system("clear")
    print("Forge Server Creator:\n\n1. Install\n2. Repair/Reinstall\n\n")
    actionchoice = input(">>> ")
    