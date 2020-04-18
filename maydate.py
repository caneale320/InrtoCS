# Caleb Neale, can4ku


def creepy(younger, older):
    too_young = younger < (older/2)+7
    too_old = (younger*2)+13 < older
    return too_young or too_old


