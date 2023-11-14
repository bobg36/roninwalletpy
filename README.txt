main_marketplace.py
all market functions and wallet variables are imported at top of file. Interact with marketplace using this file

marketCommands.py
.js scripts are wrapped in python functions here.

marketFunctions.py
helper functions, e.g grabbing egg id from GraphQL endpoints, or axieIds from text file

All Functions:
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
