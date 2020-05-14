import xlrd

wb = xlrd.open_workbook("work-time.xls")
ws = wb.sheet_by_index(0)
row_cnt = ws.nrows
col_cnt = ws.ncols
work_time = 0

for index in range(0, row_cnt):
    start_time = xlrd.xldate_as_tuple(ws.cell_value(index, col_cnt - 2), wb.datemode)
    finish_time = xlrd.xldate_as_tuple(ws.cell_value(index, col_cnt - 1), wb.datemode)
    if finish_time[3] >= 18:
        work_time += finish_time[3] - start_time[3] + (finish_time[4] - start_time[4]) / 60 - 0.5 - 1.5
    elif finish_time[3] == 17 and finish_time[4] >= 30:
        work_time += finish_time[3] - start_time[3] + (finish_time[4] - start_time[4]) / 60 - (finish_time[4] - 30) / 60 - 1.5
    elif finish_time[3] == 17 and finish_time[4] < 30:
        work_time += finish_time[3] - start_time[3] + (finish_time[4] - start_time[4]) / 60 - 1.5

avg_work_time = work_time / row_cnt
print(avg_work_time)