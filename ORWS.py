import mysql.connector
import pandas as pd
import numpy as np

RiverDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "fauxpswd",
    database = "riverData"
)

mycursor = RiverDB.cursor()

ORWS = pd.read_csv('/Users/ianmonroe/Desktop/USGS API/data/ORWS.csv')

cols = ORWS.columns.tolist()

ORWS = ORWS.loc[:,['OBJECTID','RIVER_ID','SEGMENT_ID','GNIS_NAME','CLASSIFICATION','SEGMENT_MILES','TOTAL_MILES','BEGINNING_POINT_NARRATIVE','ENDING_POINT_NARRATIVE','AGENCY','ADMINISTRATIVE_UNIT','COUNTY','SHAPELEN','State']]
print(ORWS)


ORWS = ORWS.where((pd.notnull(ORWS)), None)
ORWS = ORWS.fillna('')
print(ORWS)

for i, row in ORWS.iterrows():
    insertORWS = ('INSERT INTO riverData.ORWS (ObjectID,RiverID,SegmentID,RiverName,Classification,SegmentMi,Totalmi,Beginning,Ending,Agency,AdminUnit,County,Shapelen,State) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    mycursor.execute(insertORWS,tuple(row))
print("Hoorah")

RiverDB.commit()
