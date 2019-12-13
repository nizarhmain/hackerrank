s = "00:05:45AM"
def convert(s):
    stuff = s.split(':')
    modality = stuff[-1][2]
    first = int(stuff[0])
    if modality == 'P' and first == 12:
        stuff[0] = '12'
        return str(':'.join(stuff)[:-2])
    if modality == 'P' and first != 12:
        stuff[0] = str(first + 12 % (first+12))
    else:
        stuff[0] = str((first % 12)).rjust(2, '0')
    return str(':'.join(stuff)[:-2])
print(convert(s))