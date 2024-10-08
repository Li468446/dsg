import jinja2

# 数据集
# 包含标签和数据集，用于绘制饼图
data = {
    'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],  # 标签名称
    'datasets': [{
        'data': [12, 19, 3, 5, 2, 3],  # 每个标签对应的数据值
        'backgroundColor': ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']  # 背景颜色
    }]
}

# 配置项
# 设置图表的一些基本属性
options = {
    'responsive': True,  # 图表是否响应式
    'maintainAspectRatio': False,  # 是否保持宽高比
    'scales': {
        'y': {'beginAtZero': True}  # y轴从零开始
    }
}

# HTML模板
# 定义HTML模板，包含饼图的JavaScript代码
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>扇形图示例</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>  # 引入Chart.js库
</head>
<body>
    <canvas id="myChart" width="400" height="400"></canvas>  # 创建画布元素
    <script>
        var ctx = document.getElementById('myChart').getContext('2d');  # 获取画布上下文
        var myChart = new Chart(ctx, {  # 创建Chart对象
            type: 'pie',  # 图表类型为饼图
            data: {{ data|tojson }},  # 数据集
            options: {{ options|tojson }}  # 配置项
        });
    </script>
</body>
</html>
"""

# 使用Jinja2环境渲染模板
env = jinja2.Environment()  # 创建Jinja2环境
html_content = env.from_string(template).render(data=data, options=options)  # 渲染模板

# 将生成的HTML内容保存到文件
with open('pie_chart.html', 'w', encoding='utf-8') as f:
    f.write(html_content)  # 写入HTML内容
