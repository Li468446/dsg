import numpy as np

# 生成示例数据
np.random.seed(0)  # 确保每次运行时生成相同的数据
categories = ['Category {}'.format(i) for i in range(500)]  # 假设有500个分类
values = np.random.rand(500) * 100  # 每个分类随机生成一个0到100之间的值
import plotly.graph_objs as go

# 创建柱形图
fig = go.Figure(data=[go.Bar(
    x=categories,
    y=values
)])

# 设置图表标题和轴标签
fig.update_layout(
    title='大数据面板',
    xaxis_title='类别',
    yaxis_title='数值',
    xaxis_tickangle=-45  # 旋转x轴标签以适应大量文本
)

# 将图表保存为HTML文件
fig.write_html("big_data_bar_chart.html")
