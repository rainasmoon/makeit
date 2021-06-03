import csv
import urllib.parse


with open('all-stock.csv', newline='') as f:
    reader = csv.reader(f)
    writer = open('content/all-stocks.md', 'w')
    writer.write('Title: A股诚信档案查询\n')
    writer.write('Date: 2021-06-03 10:42\n')
    writer.write('Category: 诚信\n')
    writer.write('\n')
    writer.write(' | 股票代码 | 简称 | 公司全称 | \n')
    writer.write(' | -------- | ---- | -------- | \n')
    for row in reader:
        if row[2] == 'symbol':
            continue
        writer.write(' | ' + row[2] + ' | ' + row[3] + ' | <a href="https://www.creditchina.gov.cn/xinyongxinxi/index.html?index=0&scenes=defaultScenario&tableName=credit_xyzx_tyshxydm&searchState=2&entityType=1,2,4,5,6,7,8&keyword='
                     + urllib.parse.quote(row[6]) + '" target="_blank">' + row[6] + '</a>  | \n')

