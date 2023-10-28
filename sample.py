def dataParameters(fromY, untillY,data):
    if fromY in data and untillY:
        if int(fromY) < int(untillY):
            pass
    else:
        raise Exception ("Year not found")