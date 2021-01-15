from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time
from colorama import Fore


banner = ("""

░██████╗░██████╗░░█████╗░██████╗░██╗░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚════██║
██║░░██╗░██║░░██║██║░░██║██████╔╝█████═╝░░░███╔═╝
██║░░╚██╗██║░░██║██║░░██║██╔══██╗██╔═██╗░██╔══╝░░
╚██████╔╝██████╔╝╚█████╔╝██║░░██║██║░╚██╗███████╗
░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝ """)

print("\n")
for col in banner:
    print(Fore.GREEN + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("                              Profile: https://github.com/ShantanuRauthan\n ")
for col in x:
    print(Fore.YELLOW + col, end="")
    sys.stdout.flush()
    time.sleep(0.0030)

try:
    data = input("\n[+] Save Results in a File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Enter The Dork: ")
        amount = input("[+] Enter The Number Of Websites To Display: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            

    print ("[•] Done... Exiting...")
    sys.exit()
# =====# Main #===== #
if __name__ == "__main__":
  dorks()
