

class File_Functions():

    def WriteCsv(csvDir, csvMsg):

        with open(csvDir, "a+") as csvFile:

            csvFile.write(csvMsg)
            csvFile.close