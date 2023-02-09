import mysql.connector
import pandas as pd

RiverDB = mysql.connector.connect(
   host = "localhost",
   user = "root",
   passwd = "Gnarlycarly97@",
   database = "riverdata"
)

mycursor = RiverDB.cursor()

mycursor.execute("CREATE TABLE River(siteID int, CFS smallint NOT NULL, Date DATE PRIMARY KEY);")
mycursor.execute("INSERT INTO River (siteID,CFS,Date) VALUES(%s,%s,%s)",(14103000,4460,"2022-2-5"))
 
data12 = pd.read_csv('/Users/ianmonroe/Desktop/1410300 2622-2723.csv', index_col=False, delimiter = ',')
data1 = pd.DataFrame(data12)
data1 = data1.drop(columns = ['Unnamed: 3', 'Unnamed: 4'])
data1 = data1.reindex(columns=['siteID','CFS','DATE'])
print(data1)

print(data1.columns.tolist())


for i, row in data1.iterrows():
   insertdata = "INSERT INTO riverdata.River VALUES (%s,%s,%s)"
   mycursor.execute(insertdata, tuple(row))
print("Inserted!")

RiverDB.commit()
mycursor.execute("SELECT * FROM riverdata.River")