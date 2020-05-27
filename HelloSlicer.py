print("HelloSlicer")

from FileReader.IgesReader import IgesReader
from FileReader.STLReader import STLReader

r = IgesReader(r'FileReader\TestFiles\EyepieceHolder.IGS')
r.generatePath()