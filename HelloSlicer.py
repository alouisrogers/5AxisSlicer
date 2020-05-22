print("HelloSlicer")

from FileReader.STLReader import STLReader
from FileReader.MFReader import MFReader

file = 'FileReader/TestFiles/3DBenchy.3mf'

if(file[-4:].upper() == '.STL'):
    print("stl file")
    r = STLReader(file)
    r.generatePath()

elif(file[-4:].upper() == '.3MF'):
    print("3MF file")
    r = MFReader(file)

else:
    print("invalid file format")

