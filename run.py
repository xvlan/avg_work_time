# -*- coding:utf-8 -*-

import json
import datetime


def get_time(date, start_time, finish_time):
    Y = int(date.split('-')[0])
    M = int(date.split('-')[1])
    D = int(date.split('-')[2])
    start_time_H = int(start_time.split(':')[0])
    start_time_F = int(start_time.split(':')[1])
    start_time_S = 0

    finish_time_H = int(finish_time.split(':')[0])
    finish_time_F = int(finish_time.split(':')[1])
    finish_time_S = 0

    t1 = datetime.datetime(Y, M, D, start_time_H, start_time_F, start_time_S)
    t2 = datetime.datetime(Y, M, D, finish_time_H, finish_time_F, finish_time_S)
    total_time = t2 - t1
    if start_time_H <= 12 and finish_time_H >= 14 and finish_time_H < 18:
        total_time -= datetime.timedelta(hours=2)
    elif start_time_H <= 12 and finish_time_H >= 14 and finish_time_H == 18 and finish_time_F < 30:
        total_time -= datetime.timedelta(hours=(2 + (finish_time_F / 60)))
    elif start_time_H <= 12 and finish_time_H >= 14 and finish_time_H == 18 and finish_time_F >= 30:
        total_time -= datetime.timedelta(hours=(2 + 0.5 ))
    elif start_time_H <= 12 and finish_time_H >= 14 and finish_time_H >= 19:
        total_time -= datetime.timedelta(hours=(2 + 0.5))
    return total_time

def get_avg_time(time_list):
    return 

if __name__ == "__main__":
    fp = open('time.json', 'r', encoding='UTF-8')
    time_ori = json.load(fp)

    print("姓名\t\t\t日期\t\t\t\t上班时间\t\t下班时间\t\t当天工时")
    for line in time_ori.get('Rows'):
        print(line.get('lastName') + '\t\t', end='')
        print(line.get('showRecordDate') + '\t\t', end='')
        print(line.get('showBeginTime') + '\t\t', end='')
        print(line.get('showEndTime') + '\t\t', end='')
        day_time = get_time(line.get('showRecordDate'), line.get('showBeginTime'), line.get('showEndTime'))
        print(day_time)