# -*- coding: utf-8 -*-
import pdftables_api

# go to https://pdftables.com/pdf-to-excel-api
# Great work
c = pdftables_api.Client('07bkfkqw170a')
c.xlsx('Sportpesa __ Get in the Game.pdf', 'output.xlsx')