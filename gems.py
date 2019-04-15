import requests
import re

url = 'http://www.csgnetwork.com/gemchar.html'
html = requests.get(url)

table_start = '<TABLE WIDTH=80% ALIGN=CENTER BORDER=2 CELLPADDING=5>'
table_end = '</table></td></tr>'

temp = html.text.split(table_start)[1]
html_table = temp.split(table_end)[0]


temp = re.sub('</TD>(<TD ALIGN=CENTER>)?', ',', html_table)
# temp = re.sub('</TR>\n\n\t\t\t', '', temp)
temp = re.sub('</TR>', '', temp)
temp = re.sub('<TR BGCOLOR=(#[A-Z0-9]{6})>\n\n\t\t\t\t\t', '\\1,', temp)
temp = re.sub('<TD ALIGN=CENTER>', '', temp)
temp = re.sub('<font color="#[A-Z0-9]{6}">', '', temp)
temp = re.sub('</font>', '', temp)
temp = re.sub('</?b>', '', temp)
temp = re.sub('#B6D4D2', 'Gemstone Color', temp)
temp = re.sub('\t\t', '', temp)
temp = re.sub('\n\n\t \n\n\t', '\n', temp)
temp = re.sub('\n\n\t', '\n', temp)
temp = re.sub('\n   ', '', temp)
temp = re.sub(' #', '#', temp)
temp = re.sub(' Mohs', '', temp)
# temp = re.sub('[0-9]+ ?- ?[0-9]+', ',', temp)

print(temp)
