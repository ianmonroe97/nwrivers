import mysql.connector
import pandas as pd

RiverDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "fauxpswd",
    database = "riverData"
)
mycursor = RiverDB.cursor()

OregonRivers = pd.read_csv("/Users/ianmonroe/Desktop/USGS API/data/OregonRivers.csv", index_col=False, delimiter = ',')
ORdata = pd.DataFrame(OregonRivers)
ORdata.columns = ['RiverID','RiverName','RiverBasin']

print(ORdata.columns.tolist())

for i, row in ORdata.iterrows():
    insertORdata = "INSERT INTO riverData.OregonRivers (RiverID,RiverName,RiverBasin) VALUES (%s,%s,%s)"
    mycursor.execute(insertORdata, tuple(row))
print("Success!")

mycursor.execute("UPDATE OregonRivers SET State = "Oregon" WHERE State IS NULL")

RiverDB.commit()
mycursor.execute("SELECT * FROM riverData.OregonRivers")

