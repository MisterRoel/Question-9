def deposit_widthdrawal(balList):
    multiBal = []
    for bal in balList:
        if typeOf(bal) == list:
            for subbal in bal:
                if subbal < 0:
                    subbal.append(multiBal)
                return multiBal
