#calling js scripts to interact with marketplace

import subprocess
import re
import marketFunctions as mf

wallet_bob = 2
wallet_jade = 3
wallet_blessing = 4
wallet_dan = 5
wallet_juhansen = 6
wallet_axiebobshop = 7

address_bob = "ronin:f6e37c7ddf7bed40a5c847adf95589869c5c115b"
address_jade = "ronin:73c2abfdd9aa1218122f22024aa22afd82a7542d"
address_blessing = "ronin:b4367810619a19df392a823fec06725bf652d594"
address_dan = "ronin:c0d95423ca1b97d046874f86a1b56cfc14c48b04"
address_juhansen = "ronin:5cf795606a2e7091b935c42c037a4758dc00e681"
address_axiebobshop = "ronin:dc683a32553d8de5828ec1364df4b7ae6f98a66b"
address_ivy = "ronin:d8a7e07286e35dbcc6bb1c8bfa1ca758272fe130"

# unlistAxie(axieId)                                    [axieId: int]
# unlistAxies(axieId_list)                              [axieId_list: list of ints]
# listAxie(axieId, priceEth)                            [axieId: int], [priceEth: float]
# listAuction(axieId, startPrice, endPrice, duration)   [axieId: int], [startPrice: float], [endPrice: float], [duration: int(days)]
# transferAxie(axieId, transferRonin)                   [axieId: int], [transferRonin: ronin address starting with 'ronin:']
# transferAxies(axieId_list, transferRonin)             [axieId_list: list of ints], [transferRonin-ronin address starting with 'ronin:']
# selectWallet(wallet_index)                            [wallet_index: int, defined at top]
# buyAxie(axieId)                                       [axieId: int]
# hatchAxies(Ronin)                                     [Ronin: ronin address starting with 'ronin:']
# relistAxie(axieId, priceEth)                          [axieId: int], [priceEth: float]
# relistAuction(axieId, startPrice, endPrice, duration) [axieId: int], [startPrice: float], [endPrice: float], [duration: int(days)]
# getBalance                                            gets balance of current selected wallet, no args

def unlistAxie(axieId):
    argstart = "node scripts\\unlistjs\\unlistAxie.js"
    arg = argstart + " " + str(axieId)
    print(arg)
    subprocess.run(arg, shell=True, check=True)

def unlistAxies(axieId_list):
    for axieId in axieId_list:
        unlistAxie(axieId)
    
def listAxie(axieId, priceEth):
    argstart = "node scripts\\listjs\\listAxie.js"
    arg = argstart + " " + str(axieId) + " " + str(priceEth)
    print(arg)
    subprocess.run(arg, shell=True, check=True)

def listAuction(axieId, startPrice, endPrice, duration):
    argstart = "node scripts\\listjs\\listAuction.js"
    arg = argstart + " " + str(axieId) + " " + str(startPrice) + " " + str(endPrice) + " " + str(duration)
    print(arg)
    subprocess.run(arg, shell=True, check=True)

def transferAxie(axieId, transferRonin):
    argstart = "node scripts\\transferjs\\transferAxie.js"
    arg = argstart + " " + transferRonin + " " + str(axieId)
    print(arg)
    subprocess.run(arg, shell=True, check=True)

def transferAxies(axieId_list, transferRonin):
    argstart = "node scripts\\transferjs\\transferAxie.js " + transferRonin
    axieId_strings = mf.get_axieIdstring_from_list(axieId_list)  
    arg_axieIds = " ".join(axieId_strings)
    arg = argstart + " " + arg_axieIds
    print(arg)
    subprocess.run(arg, shell=True, check=True)

def buyAxie(axieId):
    argstart = "node scripts\\buyjs\\buyAxie.js"
    arg = argstart + " " + str(axieId)
    print(arg)
    subprocess.run(arg, shell=True, check=True)

def hatchAxies(Ronin):
    axieIds = mf.grab_incubated_list(Ronin)
    print('hatching: ' + str(len(axieIds)) + ' eggs')
    axieId_strings = mf.get_axieIdstring_from_list(axieIds)
    argstart = "node scripts\\hatchjs\\hatchAxie.js"
    arglist = []
    for axieId in axieId_strings:
        arg = argstart + " " + axieId + ";"
        arglist.append(arg)
    for arg in arglist:
        print("command: " + arg)
        subprocess.run(arg, shell=True, check=True)
    print('hatched: ' + str(len(axieIds)) + ' eggs')
    
def getBalance():
    arg = "node scripts\\accountsjs\\balance.js"
    # result = subprocess.run(arg, shell=True, check=True)
    result = subprocess.run(arg, shell=True, text=True, stdout=subprocess.PIPE)
    output = result.stdout
    print(output)
    output = output.split("\n")
    balance = {}
    for item in output[0:5]:
        item = item.split(" ")
        key, value = item[1], item[0]
        balance[key] = value
    balance[item[1]] = item[0]
    return balance

def selectWallet(wallet_index):
    with open('env.txt', 'r') as file:
        env_contents = file.readlines()
        keyraw = env_contents[wallet_index]
        key = re.findall('"([^"]*)"', keyraw)
        key = key[0]
        env_contents[0] = key + '\n'
    with open('env.txt', 'w') as file:
        file.writelines(env_contents)
    wallet_mapping = {
        2: "Bob New Main",
        3: "Jade",
        4: "Blessing",
        5: "Dan",
        6: "Juhansen",
        7: "Axie Bob Shop"
    }
    if wallet_index in wallet_mapping:
        print('Currently logged in to: ' + wallet_mapping[wallet_index])
    command = 'node scripts\\accountsjs\\accounts.js'
    subprocess.run(command, shell=True, check=True)

def relistAxie(axieid, priceEth):
    unlistAxie(axieid)
    while True:
        try:
            listAxie(axieid, priceEth)
            break
        except:
            print("If unlisting was successful, must wait for Axie to be completely off market. Trying again.")

def relistAuction(axieid, priceStart, priceEnd, duration):
    unlistAxie(axieid)
    while True:
        try:
            listAuction(axieid, priceStart, priceEnd, duration)
            break
        except:
            print("If unlisting was successful, must wait for Axie to be completely off market. Trying again.")
