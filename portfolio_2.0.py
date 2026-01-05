import time
import graphique

panier={}
print(graphique.un)
time.sleep(2) # pause 2 secondes
print('\n' * 100)
print(graphique.deux)
time.sleep(2) # pause 3 secondes
print('\n' * 100)
while True:
    valid=input(graphique.trois)
    print('\n' * 100)
    if valid == "q" or valid == "Q":
        print(f"Merci d'avoir utiliser mon programme voilà un récapitulatif des compétence valider {panier}")
        break
    elif valid == "ASCII" or valid == "ascii":
        input(graphique.soixantedix)
        print('\n' * 100)
        panier[valid]="70%"
    elif valid == 'OSx' or valid == 'Mac OS X' or valid == 'macOS' or valid == 'Mac' or valid == 'IOS' or valid == 'mac':
        input(graphique.quatrevinghdix)
        print('\n' * 100)
        panier[valid]="90%"
    elif valid == "Python" or valid == "python" or valid == "Monty Python's Flying Circus" :
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier[valid]="80%"
    elif valid == "Virtualisation" or valid == "virtualisation":
        input(graphique.soixantedix)
        print('\n' * 100)
        graphique.panier[valid]="70%"
    elif valid == "Windows xp":
        input(graphique.cinquante)
        print('\n' * 100)
        panier[valid]="50%"
    elif valid == "Windows 7":
        input(graphique.quatrevinghdix)
        print('\n' * 100)
        panier[valid]="90%"
    elif valid == "Windows 98":
        input(graphique.trente)
        print('\n' * 100)
        panier[valid]="30%"
    elif valid == "MS-DOS":
        input(graphique.trente)
        print('\n' * 100)
        panier[valid]="30%"
    elif valid == "Windows Vista":
        input(graphique.cinquante)
        print('\n' * 100)
        panier[valid]="50%"
    elif valid == "Window 8.1":
        input(graphique.soixantedix)
        print('\n' * 100)
        panier[valid]="70%"
    elif valid == "Windows 10" or valid == "windows X" or valid == "windows 10":
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier[valid]="80%"
    elif valid == "Windows 11" or valid == "windows 11":
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier[valid]="80%"
    elif valid == "Debian":
        input(graphique.vingt)
        print('\n' * 100)
        panier[valid]="20%"
    elif valid == "Ubuntu":
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier[valid]="80%"
    elif valid == "VirtualBox" or valid == "Virtualbox" or valid == "virtualBox" :
        input(graphique.soixantedix)
        print('\n' * 100)
        panier[valid]="70%"
    elif valid == "UTM" or valid == "utm" or valid == "Utm" :
        input(graphique.trente)
        print('\n' * 100)
        panier[valid]="30%"
    elif valid == "Visual Studio Code" or valid == "Visual studio code" or valid == "visual studio code":
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier[valid]="80%"
    elif valid == "Sublime Text" or valid == "Sublime text" or valid == "sublime text":
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier[valid]="80%"
    elif valid == "Tor Browser" or valid == "Tor" or valid == "The Tor Project":
        input(graphique.cinquante)
        print('\n' * 100)
        panier[valid]="50%"
    elif valid == "PyCharm" or valid == "Pycharm" or valid == "pycharm" or valid == "PyCharm CH2":
        input(graphique.soixantedix)
        print('\n' * 100)
        panier["PyCharm"]="70%"
    elif valid == "CSS" or valid == "css":
        input(graphique.cinquante)
        print('\n' * 100)
        panier["CSS"]="50%"
    elif valid == "html" or valid == "HTML":
        input(graphique.quatrevingt)
        print('\n' * 100)
        panier["HTML"]="80%"
    elif valid == "C#" or valid == "c#":
        input(graphique.quarente)
        print('\n' * 100)
        panier["C#"]="40%"
    else:
        input(graphique.oups)
        print('\n' * 100)
