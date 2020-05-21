

class STLReader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(self.filepath)
        self.fileContents = self.file.read()
        self.file.close()
        print(len(self.fileContents))

        pathVisualOBJ = []

    def generatePath(self):
        fileContents = self.fileContents.split('facet')
        i = 0
        while(i < len(fileContents)):
            if fileContents[i] == '\n':
                fileContents.remove(i)
            i = i+1
        print(fileContents)

    def generateGCode(self):
        return
