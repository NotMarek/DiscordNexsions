import requests, random, json
from colorama import init, Fore
init(convert=True, autoreset=True)


def info():
    info = {}
    print(f"{Fore.CYAN} Please input your discord tokens")
    info["token"] = str(input(" > "))
    print(f"{Fore.CYAN} Please input your desired method: [battlenet, skype, leagueoflegends, contacts]")
    info["option"] = str(input(" > "))
    print(f"{Fore.CYAN} Input the amount of connections you'd like")
    while 'amount' not in info:
        try:
            info["amount"] = int(input(" > "))
        except ValueError:
            print(f'{Fore.RED}That was not a number :( try again.')
    print(f"{Fore.CYAN} Input the desired name")
    info["name"] = str(input(" > "))
    return info


def start():
    information = info()
    for i in range(information["amount"]):
        req = requests.put(f'https://discordapp.com/api/v6/users/@me/connections/{information["option"]}/{random.randint(1, 10)}',
        json={
            "name": information["name"],
            "visibility": 1,
            "verified": True
            },
        headers={
            "Content-Type": "application/json",
            "Authorization": str(information["token"])
            })
        try:
            if json.loads(req.text)["type"] == information["option"]:
                print(f"{Fore.GREEN} Successfully added the new connection")

        except KeyError:
            print(f"{Fore.RED} An error occured. On token: {information['token']}")


if __name__ == "__main__":
    start()
