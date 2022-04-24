

import json
import requests
C='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=1000'
data2 = requests.get(C)
S = data2.text
D = json.loads(S)

area = input('輸入欲查詢的區域:')
for row in D:
    if area == str(row['sarea']):
        print('站名:',row['sna'])
        print('可借用:',row['sbi'],'輛')
        print('可停放:',row['bemp'],'輛')
print('程式執行完畢')




 
    
    
