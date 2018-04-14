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
    <center></br>

    </center>
    """
gf_procs.set_header(1)
run_date = '2018-02-07'
tier = ['GOLD','SILVER','BRONZE']
color = ['rgb(225, 180, 90)','rgb(204, 204, 204)','rgb(170, 136, 68)']
print('<br><center><table style="width: 80%; font-family: Arial,Helvetica,sans-serif; font-size: large; text-transform: capitalize;"><tbody><tr>')
for x in range(1,4):
    print('<td style="vertical-align: top; width: 33%;">')
    print('<table style="width: 100%; text-align: left; margin-left: auto; margin-right: auto; border="3" cellpadding="1">')
    print('<tr style="font-weight: bold;">')
    print('<td colspan="2" style="text-align: center; background-color: '+color[x-1]+';">'+tier[x-1]+'</td>')
    print('</tr>')
    print('<tr>')
    print('<td style="font-weight: bold; font-style: italic;"><small>Player</small></td>')
    print('<td style="font-weight: bold; font-style: italic;"><small>KTD</small></td>')
    print('</tr>')

    tier_stats = gf_procs.get_data('playerTier',x, run_date)
    for row in tier_stats:
        try:
            print('<td>'+row.playerDisplayName+'</td><td>'+str(round((row.KTD),2))+'</td>')
        except:
            continue
        print('</tr>')
    print('</table></td>')
print('</table>')
print(htmlFormat)
gf_procs.set_footer()
