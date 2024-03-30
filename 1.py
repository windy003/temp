from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# 设置云服务商和认证信息
cls = get_driver(Provider.AWS)
driver = cls('access key', 'secret key', region='us-east-1')

# 连接成功后可以进行其他操作，例如列出所有服务器
nodes = driver.list_nodes()
for node in nodes:
    print(node.name)
