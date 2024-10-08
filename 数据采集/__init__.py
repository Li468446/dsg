import requests
import time

# 定义拉勾网职位搜索的API URL
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

# 设置请求头，模拟浏览器行为，绕过反爬虫机制
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
    "referer": "https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput=",
    "origin": "https://www.lagou.com",
    "cookie": "RECOMMEND_TIP=true; user_trace_token=20210118143031-ede97a5b-77bd-4487-a492-d1121f24ff62; LGUID=20210118143031-ff294a5f-41fb-4627-83c4-41343998f128; _ga=GA1.2.1737742795.1610951427; JSESSIONID=ABAAABAABAGABFAF65FCDBA86B0BDB8642A0A207813F54D; WEBTJ-ID=20210418%E4%B8%8A%E5%8D%8810:48:57104857-178e2e195248-0fc970dddb106c-d7e1938-1440000-178e2e1952514; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; privacyPolicyPopup=false; _gat=1; LGSID=20210418104907-d83a2861-91e1-45e1-9393-d54197221c2d; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D02003390%5F42%5Fhao%5Fpg%26ie%3Dutf-8%26wd%3Dlagou; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617717436,1617719456,1617782807,1618714139; _gid=GA1.2.90038644.1618714139; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; __lg_stoken__=5daaeb170a87fb743bddb84557aa24c4295e42b2af50f9237b9015a10142c2eb6ff36389cbddaa671b715511101a6f5b07f6329469455ca6b1b231bc2ca6ccfb73489b0a3401; X_HTTP_TOKEN=ab94b9f45077f14e4614178161e2224e9205fea79c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217714300602ae-088bb004b54025-303464-1440000-177143006033a8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22lagou%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fs%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2290.0.4430.72%22%7D%2C%22%24device_id%22%3A%2217714300602ae-088bb004b54025-303464-1440000-177143006033a8%22%7D; LGRID=20210418104925-a283ca0d-154d-4dcd-b18f-3c1eced0c71e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1618714157; SEARCH_ID=76d0bb86d8dd4ec08baba352d6b41e5d"
}

# 定义搜索参数，搜索关键词为'大数据'
data = {
    'first': 'true',
    'pn': '1',
    'kd': '大数据'
}

# 循环爬取第25到31页的职位信息
for i in range(25, 31):
    # 更新搜索参数中的页码
    data['pn'] = i

    # 发送POST请求
    resp = requests.post(url, headers=headers, data=data)

    # 获取响应文本
    result = resp.text

    # 将结果保存到文件
    with open(f'lagou/{i}.json', mode='w', encoding='utf-8') as f:
        f.write(result)
        print(result)

    # 模拟人类浏览行为，避免被封IP
    time.sleep(5)
