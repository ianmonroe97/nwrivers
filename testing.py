"""
Name: Ian Monroe
Date: 02/06/2022
Purpose:
    Using this file to create functions that will be used in main.py
    first function, use requests to grab data
"""
#use this space to import modules/libraries
import requests,json

#Define Path
mainPath = '/Users/ianmonroe/Desktop/USGS API'
pythonPrograms = "%s/pythonPrograms" %(mainPath)
workingDir = "%s/working"%(mainPath)
dataDir =  "%s/data" %(mainPath)
'''
 #test url

url = 'https://waterservices.usgs.gov/nwis/iv/?format=json&sites=14103000&parameterCd=00060,00065&siteStatus=all'

r = requests.get(url)
print(r.status_code)
'''
def getData(stationID):
    print("Grabbing Data From StationID: %s " % stationID)
    print("----------------------------")
    #Build URL Below
    url = ("https://waterservices.usgs.gov/nwis/iv/?format=json&sites=%s&parameterCd=00060,00065&siteStatus=all")% stationID
    r = requests.get(url)
    if r.status_code != 200:
        print("Request Failed, status code : %s"%(r.status_code))
    else:
        print("Requests good to go!: %s "%(r.status_code))
    data = r.json()
    #save dictionary into workingDir
    #path to workingDir Users/ianmonroe/Desktop/USGS API
    with open("%s/%s.txt"%(workingDir,stationID), "w") as saveFile:
        json.dump(data,saveFile)
    print("function complete data stored in %s/%s.txt" %(workingDir,stationID))
    print("----------------------------------------------------")


def groomData(stationID):
    with open("%s/%s.txt"%(workingDir,stationID),"r") as openFile:
        data = json.load(openFile)

        riverDateTime = (data["value"]["timeSeries"][0]["values"][0]["value"][0]["dateTime"])
        riverCFS = (data["value"]["timeSeries"][0]["values"][0]["value"][0]["value"])

        saveDict = {"CFS":riverCFS,"DATETIME":riverDateTime}


        #create masterfile from list
        with open("%s/final_%s.txt" %(dataDir,stationID), "w") as saveFile:
            json.dump(saveDict,saveFile)

