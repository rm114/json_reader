import json
lst = open("json_file.py", "r")
aliases = []
ncbiGeneID = []
approvedSymbol = []
previousSymbols = []
groupName = []
approvedName = []


for x in lst:
    y = json.loads(x)
    for z in y:
        None
        
        try:
            ncbiGeneID.append(z['ncbiGeneID'])
        except:
            ncbiGeneID.append("-")
        try:
            approvedSymbol.append(z['approvedSymbol'])
        except:
            approvedSymbol.append("-")
        try:
            aliases.append(z['aliases'])
        except:
            aliases.append("-")
        try:
            previousSymbols.append(z['previousSymbols'])
        except:
            previousSymbols.append("-")
        try:
            groupName.append(z['groupName'])
        except:
            groupName.append("-")
        try:
            approvedName.append(z['approvedName'])
        except:
            approvedName.append("-")


for item in aliases:
    print(*item, sep=', ')
for item in ncbiGeneID:
    print(item)
for item in approvedSymbol:
    print(*item, sep='')
for item in previousSymbols:
    print(*item, sep='')
for item in groupName:
    print(*item, sep='')
for item in approvedName:
    print(*item, sep='')
quit()