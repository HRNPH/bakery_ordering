import pandas as pd
# read csv
df = pd.read_csv('data/data.csv')

file = open("result.txt", "w+" , encoding="utf-8")

acctext = "สะดวกโอน 3922431482 ธ.ไทยพาณิชย์ ชื่อ เหมวรรณ"

# loop through each row in df
# for index, row in df.iterrows():
#     # write to file
#     pay = (int(row['hokkai']) +  int(row['butter']) + int(row['mamon']))
#     file.write(f"{row['name']} ส่งที่:{row['location']} \n เบอร์:{row['phone']} \n ฮอกไกโด:{row['hokkai']} บัตเตอร์:{row['butter']} มาม่อน:{row['mamon']} \n ต้องจ่าย:{pay}บาท \n {acctext}")

for i in range(df.shape[0]):
    row = df.loc[i]
    pay = (((int(row['hokkai']) +  int(row['butter']))* 20) + (int(row['mamon']) * 15))
    file.write(f"{row['name']} ส่งที่:{row['location']} \nเบอร์:{'ไม่มี' if row['phone'] == 0 else row['phone']} \nฮอกไกโด:{row['hokkai']} บัตเตอร์:{row['butter']} มาม่อน:{row['mamon']} \nต้องจ่าย:{pay}บาท \n{acctext}")
    file.write('\n \n')