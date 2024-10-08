import jinja2

# 数据集
data = {
    'categories': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'values': [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
}

# 配置项
options = {
    'title': {
        'text': '折线图'
    },
    'tooltip': {
        'trigger': 'axis'
    },
    'legend': {
        'data': ['数据']
    },
    'xAxis': {
        'type': 'category',
        'data': data['categories']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [
        {
            'name': '数据',
            'type': 'line',
            'data': data['values']
        }
    ]
}

# HTML模板
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ECharts 折线图示例</title>
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
with open('echarts_line_chart.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
