#Define paths
mainPath = '/Users/ianmonroe/Desktop/USGS API'
pythonPrograms = "%s/pythonPrograms" %(mainPath)
workingDir = "%s/working"%(mainPath)
dataDir =  "%s/data" %(mainPath)

from testing import getData

from testing import groomData
station = "14103000"

#getData(station)

groomData(station)