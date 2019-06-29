from FileHelper import FileManager
import sys

myFileManager = FileManager.FileManager()
if sys.argv[1] == "f":
    myFileManager.getLocation()
    result = myFileManager.startScan()
    myFileManager.printResults(result)          
if sys.argv[1] == "d":
    myFileManager.trashDupes()