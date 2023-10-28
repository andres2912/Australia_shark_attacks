def dataParameters(fromY, untillY,data):
    for d in data:
        if d['Year'] == " ":
            data.remove(d['Year'])
            print (data)
    if fromY in data and untillY:
        if int(fromY) < int(untillY):
            pass
    else:
        raise Exception ("Year not found")