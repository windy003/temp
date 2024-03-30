from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# 设置云服务商和认证信息
cls = get_driver(Provider.AWS)
driver = cls('access key', 'secret key', region='us-east-1')

# 创建一个新的虚拟机
image = driver.list_images()[0]  # 选择镜像
size = driver.list_sizes()[0]    # 选择规格
node = driver.create_node(name='my-instance', image=image, size=size)
print(node)
