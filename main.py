from functions import file_functions
from const import directory
from classes import item
from pathlib import Path

class Main:

    fileFunctions = file_functions.File_Functions
    constDirectory = directory.Directory

    Path(constDirectory.csvDir).mkdir(parents=True, exist_ok=True) 

    itemList = 

    for itemData in itemList:

        item = item.Item(itemList[0], itemList[1], itemList[2], itemList[3], itemList[4], itemList[5], itemList[6])

        csvContent = "%s;%s;%s;%s;%s;%s;%s\n" % (item.name, item.physicalDamage, item.magicDamage, item.fireDamage, item.lightningDamage, item.bonusDamage, item.merchant)

        fileFunctions.WriteCsv(constDirectory.csvDir + "items.csv", csvContent)
        
        
        
        


