import urllib.request


def grab(url):
    # �򿪴������ַ
    resp = urllib.request.urlopen(url)
    # ��ȡ��ҳԴ������
    data = resp .read()
    # ����洢�ļ���
    name = input("�붨���ļ���")
    # ���ļ�
    file_name = open(name, "wb")
    # ������д���ļ�
    file_name.write(data)
    # �ر��ļ�
    file_name.close()

    print("����Դ�����")

if __name__ == '__main__':
    # ���ո�ʽ������ַ
    web_addr = input("��������Ҫץȡ����ַ(����http://www.baidu.com/):")
    try:
        grab(web_addr)
    except:
        print("��ַ��������")