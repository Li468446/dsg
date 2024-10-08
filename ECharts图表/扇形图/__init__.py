import jinja2

# 数据集
data = {
    'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    'values': [12, 19, 3, 5, 2, 3]
}

# 配置项
options = {
    'title': {
        'text': '扇形图示例'
    },
    'tooltip': {},
    'legend': {
        'data': data['labels']
    },
    'series': [
        {
            'name': '访问来源',
            'type': 'pie',
            'radius': '55%',
            'data': [{'name': label, 'value': value} for label, value in zip(data['labels'], data['values'])],
            'emphasis': {
                'itemStyle': {
                    'shadowBlur': 10,
                    'shadowOffsetX': 0,
                    'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
}

# HTML模板
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ECharts 扇形图示例</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
</head>
<body>
    <div id="main" style="width: 600px;height:400px;"></div>
    <script>
        // 初始化图表
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        var option = {{ options|tojson }};

        // 使用刚指定的配置项和数据显示图表
        myChart.setOption(option);

        // 窗口大小变化时自动更新图表
        window.addEventListener('resize', function() {
            myChart.resize();
        });
    </script>
</body>
</html>
"""

# 使用Jinja2环境渲染模板
env = jinja2.Environment()
html_content = env.from_string(template).render(options=options)

# 将生成的HTML内容保存到文件
with open('echarts_pie_chart.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
