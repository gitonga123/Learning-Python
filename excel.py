# -*- coding: utf-8 -*-
import xlrd
def open_file(path):
	 book = xlrd.open_workbook(path)

	 print book.nsheets

	 # print book.sheet_names()

	 first_sheet = book.sheet_by_index(0)
	 print first_sheet.row_values(0)
	 cell = first_sheet.cell(1,1)
	 print first_sheet.row_slice(rowx=0,
                                start_colx=0,
                                end_colx=2)

path="output.xlsx"
open_file(path)