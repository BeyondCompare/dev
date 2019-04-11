#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import json
wb = xlrd.open_workbook('python_xls.xlsx')
sh = wb.sheet_by_index(0)
cell_A1 = sh.cell(0,0).value
print(cell_A1)
data_dict=json.loads(cell_A1)
for k in data_dict:
	print(k,data_dict[k])
