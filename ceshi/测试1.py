import unittest
from unittest.mock import patch, MagicMock
from plotly.graph_objs import Figure, Bar
from DemoClass import DemoClass

class TestDemoClass(unittest.TestCase):

    def setUp(self):
        self.demo = DemoClass()

    @patch('plotly.graph_objs.Figure')
    @patch('plotly.graph_objs.Bar')
    @patch('numpy.random.rand')
    @patch('numpy.array')
    @patch('numpy.arange')
    @patch('plotly.graph_objs.Figure.update_layout')
    @patch('plotly.graph_objs.Figure.write_html')
    def test_create_bar_chart(self, mock_write_html, mock_update_layout, mock_arange, mock_array, mock_rand, mock_Bar, mock_Figure):
        # 设置模拟函数的返回值
        mock_arange.return_value = range(500)
        mock_array.return_value = ['Category 0', 'Category 1', ..., 'Category 499']
        mock_rand.return_value = MagicMock()
        mock_Bar.return_value = Bar(x=['Category 0', 'Category 1', ..., 'Category 499'], y=MagicMock())
        mock_Figure.return_value = Figure(data=[mock_Bar.return_value])

        # 调用待测试的函数
        self.demo.create_bar_chart()

        # 验证mock对象是否被调用
        mock_arange.assert_called_once()
        mock_array.assert_called_once()
        mock_rand.assert_called_once()
        mock_Bar.assert_called_once()
        mock_Figure.assert_called_once()
        mock_update_layout.assert_called_once()
        mock_write_html.assert_called_once_with("big_data_bar_chart.html")

if __name__ == '__main__':
    unittest.main()
