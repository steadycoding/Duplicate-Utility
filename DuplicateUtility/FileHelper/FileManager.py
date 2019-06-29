import os, sys
from collections import defaultdict
from FileHelper.HashingManager import Hashing
from send2trash import send2trash
class FileManager(object):
    pass
    
    def getLocation(self):
        cwd = os.getcwd()
        print('Executing from directory: %s' % cwd)
        thisFile = sys.argv[0]
        print('Executing from file: %s' % thisFile)
        targetDir = sys.argv[2]
        print('Performing scan on directory: %s'  % targetDir)

    def startScan(self):
        _hashing = Hashing()
        targetDir = sys.argv[2]
        hash_dict = defaultdict(list)
        for (dirPath, _, fileNames) in os.walk(targetDir):
            for fileName in fileNames:
                value = os.path.join(dirPath,fileName)
                key = _hashing.hashFile(value)
                hash_dict[key].append(value)
        return hash_dict
    
    def printResults(self, result_dict):
        with open('DuplicateResults', 'w') as f:
            for _, values in result_dict.items():
                if len(values) > 1:
                    f.write('The following files share a hash:\n')
                    for value in values:
                        f.write('%s\n' % value)
        f.close()
    
    def trashDupes(self):
        duplicateResults = sys.argv[2]
        with open(duplicateResults, 'r') as f:
            for line in f:
                send2trash(line)
        f.close()
