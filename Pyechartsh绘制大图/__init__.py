from pyecharts.charts import Map
from pyecharts import options as opts

# 示例数据，这里假定有一些省份及其对应的访问量
data = [
    ("北京", 100), ("上海", 150), ("广东", 300),
    ("浙江", 220), ("江苏", 200), ("山东", 180),
    # 添加更多省份和数据...
]

# 创建地图实例
map_chart = Map()

# 添加数据到地图
map_chart.add("用户访问量", data, "china")

# 设置全局配置项
map_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="中国地图 - 用户访问量分布"),
    visualmap_opts=opts.VisualMapOpts(min_=100, max_=300)
)

# 渲染地图
map_chart.render("china_user_visits.html")
