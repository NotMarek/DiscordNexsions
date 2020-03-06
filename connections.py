import requests, random, json, os, easygui
from colorama import init, Fore
init(convert=True)

pause = lambda : os.system('pause')
clear = lambda : os.system("cls")

def info():

    info = {}

    print(f"{Fore.CYAN} Please input your discord tokens {Fore.RESET}")
    info["token"] = str(input(" > "))
    print(f"{Fore.CYAN} Please input your desired method: [battlenet, skype, lol, contacts] {Fore.RESET}")
    info["option"] = str(input(" > "))
    print(f"{Fore.CYAN} Input the amount of connections you'd like {Fore.RESET}")
    info["amount"] = int(input(" > "))
    print(f"{Fore.CYAN} Input the desired name {Fore.RESET}")
    info["name"] = str(input(" > "))
    return json.loads(str(info).replace("'", '"'))

def start():

    information = info()

    with requests.Session() as session:
                i = 0
                while True:
                    i+=1
                    if i < information["amount"]:
                        req = session.put(f'https://discordapp.com/api/v6/users/@me/connections/{information["option"]}/{random.randint(1, 10)}', 

                        json={
                            "name": information["name"],
                            "visibility": 1,
                            "verified": True
                            },
                        headers={
                            "Content-Type": "application/json",
                            "Content-Length": str(len(information["name"])),
                            "Authorization": str(information["token"])
                            })

                        try:
                            if json.loads(req.text)["type"] == information["option"]:
                                print(f"{Fore.GREEN} Successfully added the new connection {Fore.RESET}")
                        except:
                            print(f"{Fore.RED} An error occured. On token: {information['token']} {Fore.RESET}")   
                    else:
                        print(Fore.RED + "\n ")
                        pause()
                        exit()                                  


if __name__ == "__main__":
    start()
