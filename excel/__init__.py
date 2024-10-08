#import panadas as pd
#import matplotlib.pyplot as plt
#from packaging.tags import platform_tags

#df = pd.read_excel('销售业绩表1.xlsx')
#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axas.unicode_minus'] = False

#x1 = df['月份']
#y1 = df['销售业绩']
#y2 = df['利润']

#plt.plot(x1, y1, color='red', linewidth = 3, linestyle ='solid')
#plt.plot(x1, y2,color='black', linewidth = 3, linestyle = 'solid')
#plt.show()

#with open('pie_chart.html', 'w', encoding='utf-8') as f:
 #   f.write(html_content)  # 写入HTML内容

import pandas as pd  # 导入pandas模块
import matplotlib.pyplot as plt  # 导入matplotlib模块

df = pd.read_excel('销售业绩表1.xlsx')  # 从指定工作簿中获取数据
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为图表的中文文本设置默认字体，以避免中文显示乱码问题
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标值为复数时无法显示负号的问题

    # 指定数据中的X轴和Y轴的列
x1 = df['月份']
y1 = df['销售额']
y2 = df['利润']

    # 绘制折线图
plt.plot(x1, y1, color='red', linewidth=3, linestyle='solid')
plt.plot(x1, y2, color='black', linewidth=3, linestyle='solid')
plt.show()