#!e:/Python36/python.exe
import sys
import datetime
import pyodbc
import logging
import gf_procs

logging.basicConfig(filename='gf.log',level=logging.INFO, format='%(asctime)s %(message)s')

cnx = pyodbc.connect("DSN=geek")
cursor = cnx.cursor()

htmlFormat = """
  <center>
    
  </center>
"""

gf_procs.set_header(2)

run_date = '2018-01-07'
tier = ['GenX','GenY','GenZ']
color = ['rgb(225, 180, 90)','rgb(204, 204, 204)','rgb(170, 136, 68)']
bgcolor = ['background-color: rgba(217, 173, 43, 0.37)','rgba(204, 204, 204, 0.37)','rgba(171, 136, 34, 0.37)']
genimg = ['/genx.gif','/geny.gif','/genz.gif']
genlogo = ['/bk_genxguy.jpg','/bk_genyguy.jpg','/bk_genzguy.jpg']

print('<center><br><table style="width: 80%; font-family: Arial,Helvetica,sans-serif; font-size: large; text-transform: capitalize;"><tbody><tr>')
for x in range(1,4):
    print('<td height = "332" width = "217" style="vertical-align: top; background-image: url('+genlogo[x-1]+'); background-align: center; background-size: contain; background-repeat: no-repeat;"> ')
    #print('<td style="vertical-align: top; width: 33%;"> ')
    print('<table style="width: 100%; text-align: left; margin-left: auto; margin-right: auto; border-color: gray;"')
    print('<tr>')
    print('<tr style="font-weight: bold;">')
    print('<td colspan="2" style="text-align: center; style="vertical-align:center bottom;"><img src="'+genimg[x-1]+'" style="width: 118px; height: 39px;"></td>')
    print('</tr>')
    print('<td style="font-weight: bold; font-style: italic;"><small>Player</small></td>')
    print('<td style="font-weight: bold; font-style: italic;"><small>KTD</small></td>')
    print('</tr>')


    tier_stats = gf_procs.get_data('playerGroup',x, run_date)
    for row in tier_stats:
        try:
           print('<tr style=" background-color: '+bgcolor[1]+';">')
           print('<td style="border-bottom: 1px solid #ddd;font-weight: bold; font-size: 100%;">'+row.playerDisplayName+'</td><td style="border-bottom: 1px solid #ddd;">'+str(round((row.KTD),2))+'</td>')
        except:
            continue
        print('</tr>')

    print('</table></td>')
print('</table>')
gf_procs.set_footer()
