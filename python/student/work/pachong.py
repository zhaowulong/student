import urllib.request


def grab(url):
    # 打开传入的网址
    resp = urllib.request.urlopen(url)
    # 读取网页源码内容
    data = resp .read()
    # 输入存储文件名
    name = input("请定义文件名")
    # 打开文件
    file_name = open(name, "wb")
    # 将代码写入文件
    file_name.write(data)
    # 关闭文件
    file_name.close()

    print("下载源码完成")

if __name__ == '__main__':
    # 按照格式输入网址
    web_addr = input("请输入你要抓取的网址(例如http://www.baidu.com/):")
    try:
        grab(web_addr)
    except:
        print("网址输入有误")