from hdfs import InsecureClient

# 创建 HDFS 客户端
hdfs_client = InsecureClient("http://10.10.10.160:9870", user="root")
