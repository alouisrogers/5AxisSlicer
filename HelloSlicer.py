print("HelloSlicer")

from FileReader.STLReader import STLReader

r = STLReader('FileReader\TestFiles\Cube.STL')
r.generatePath()