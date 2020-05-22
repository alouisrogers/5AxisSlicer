from zipfile import ZipFile
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
import numpy as np

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def printElement(self):
        print("x: {} \t y: {} \t z: {}".format(self.x, self.y, self.z))

class MFReader:
    def __init__(self, filepath):
        self.filepath = filepath

        # extract xml file from 3mf file
        with ZipFile(filepath, 'r') as zip:
            zip.extract('3D/3dmodel.model')

        # parse xml file
        tree = et.parse('3D/3dmodel.model')
        root = tree.getroot()

        # extract all x,y,z attributes for each vertex
        vertices = []
        # TODO: figure out how to remove hyperlink from the attribute name (or if it is standard <- I think it's that)
        for vertex in root.iter('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}vertex'):
            vertices.append(Point(vertex.attrib['x'], vertex.attrib['y'], vertex.attrib['z']))

        # print the coordinates of each point, and copy to numpy array
        points = np.zeros((len(vertices), 3))
        for i in range(1,len(vertices)):
            # don't need to print these I know it works now
            # vertices[i].printElement()
            points[i, 0] = vertices[i].x
            points[i, 1] = vertices[i].y
            points[i, 2] = vertices[i].z

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(points[:,0], points[:,1], points[:,2])
        plt.show()




    def generatePath(self):
        return

    def generateGCode(self):
        return