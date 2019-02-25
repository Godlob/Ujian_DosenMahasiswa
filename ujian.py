import pymongo
import pandas as pd
import matplotlib.pyplot as plt

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)
newdb = mydb["Kampus"]
col1 = newdb["Dosen"]
col2 = newdb["Mahasiswa"]
df1 = pd.DataFrame(list(col1.find()))
df1 = df1.drop(['_id','bidang','matkul','nip','titel'], axis=1)
df2 = pd.DataFrame(list(col2.find()))
df2['status'] = pd.Series(['Mahasiswa','Mahasiswa','Mahasiswa'])
df2 = df2.drop(['_id','angkatan','nim','prodi'],axis=1)
df2 = df2.reindex(sorted(df2.columns), axis=1)
print(df1)
print(df2)
plt.bar(df1['nama'],df1['usia'])
plt.bar(df2['nama'],df2['usia'])
plt.grid(True)
plt.title('Usia Warga Kampus')
plt.legend(['Dosen','Mahasiswa'])
plt.show()