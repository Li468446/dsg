# 导入pyecharts库的options模块，用于配置图表样式
from pyecharts import options as opts
# 导入Line类，用于创建折线图
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
# 导入TitleOpts类，用于配置图表标题
# 创建Line对象，用于绘制折线图
line = Line()
# 设置x轴的数据，这里使用数字1到10作为x轴的刻度
line.add_xaxis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 设置y轴的数据，这里使用序列1，其值对应x轴的刻度
line.add_yaxis("Series1", [10, 20, 30, 40, 50, 60, 70])
# 设置全局配置项，包括标题等
line.set_global_opts(
    # 设置图表标题
    title_opts=TitleOpts(title="大数据可视化面板")
)
# 渲染图表到HTML文件，生成折线图
line.render("line_chart.html")