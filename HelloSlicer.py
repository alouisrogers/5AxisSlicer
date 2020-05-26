print("HelloSlicer")

from FileReader.STLReader import STLReader

r = STLReader(r'FileReader\TestFiles\3DBenchy.STL')
r.generatePath()