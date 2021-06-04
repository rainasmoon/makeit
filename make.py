import csv
import urllib.parse


with open('final.csv', newline='') as f:
    reader = csv.reader(f)
    writer = open('content/all-stock.md', 'w')
    writer.write('Title: A股诚信档案查询\n')
    writer.write('Date: 2021-06-03 10:42\n')
    writer.write('Category: 诚信\n')
    writer.write('URL:\n')
    writer.write('save_as: index.html\n')
    writer.write('\n')
    writer.write(' | 股票代码 | 简称 | 评级 | 公司全称 | 监管 |\n')
    writer.write(' | -------- | ---- | ---- | -------- | ---- |\n')
    for row in reader:
        if row[0] == 'symbol':
            continue
        writer.write(' | ' + row[0] + ' | ' + row[1] + ' | ' +row[3]  + ' | <a href="https://www.creditchina.gov.cn/xinyongxinxi/index.html?index=0&scenes=defaultScenario&tableName=credit_xyzx_tyshxydm&searchState=2&entityType=1,2,4,5,6,7,8&keyword='
                     + urllib.parse.quote(row[2]) + '" target="_blank">' +
                     row[2] + '</a>  | <a href="/'+row[0]+'.html">' + row[4] + '</a> | \n')

