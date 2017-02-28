# -*- coding: utf-8 -*-
import pdftables_api

# go to https://pdftables.com/pdf-to-excel-api
# Great work
c = pdftables_api.Client('your_api_key')
c.xlsx('your_pdf_file.pdf', 'output.xlsx')