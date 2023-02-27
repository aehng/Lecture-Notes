#!/usr/bin/env python  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

import time  	  	  
import sys  	  	  
from report import print_report  	  	  


# print_report takes a dictionary with these contents:  	  	  
rpt = {  	  	  
        'year': 2021,  	  	  

        'all': {  	  	  
            'num_areas': 0,  	  	  
            'total_annual_wages': 0,  	  	  
            'max_annual_wage': ["", 0],  	  	  
            'total_estab': 0,  	  	  
            'max_estab': ["", 0],  	  	  
            'total_empl': 0,  	  	  
            'max_empl': ["", 0],  	  	  
        },  	  	  

        'soft': {  	  	  
            'num_areas': 0,  	  	  
            'total_annual_wages': 0,  	  	  
            'max_annual_wage': ["", 0],  	  	  
            'total_estab': 0,  	  	  
            'max_estab': ["", 0],  	  	  
            'total_empl': 0,  	  	  
            'max_empl': ["", 0],  	  	  
        },  	  	  
}  	  	  

if len(sys.argv) != 2:
    print("Usage: big_data.py DATA_DIR")
    sys.exit(1)

print("Reading the databases...", file=sys.stderr)  	  	  
before = time.time()  	  	  


## Construct a dictionary of **valid** FIPS area codes
areas = {}
areafile = open(f'{sys.argv[1]}/area-titles.csv')
areafile.readline()  # throw away the CSV header line
for line in areafile:
    fields = line.strip().split(',', maxsplit=1)
    fips = fields[0][1:6]
    if fips.isdigit() and not fips.endswith('000'):
        areas[fips] = fields[1].strip('"')
areafile.close()


## Read the big CSV file and fill in the report

# Use named constants instead of "magic numbers" for readability
OWN_CODE  = 1
INDUSTRY_CODE = 2
ANNUAL_AVG_ESTABS = 8 	
ANNUAL_AVG_EMPLVL = 9 	
TOTAL_ANNUAL_WAGES = 10

singlefile = open(f'{sys.argv[1]}/2021.annual.singlefile.csv')
singlefile.readline()  # throw away the CSV header line
for line in singlefile:
    fips = line[1:6]
    if fips in areas:
        fields = line.split(',')
        if fields[OWN_CODE] == '"0"' and fields[INDUSTRY_CODE] == '"10"':
            rpt['all']['num_areas'] += 1

            wages = int(fields[TOTAL_ANNUAL_WAGES])
            rpt['all']['total_annual_wages'] += wages
            if wages > rpt['all']['max_annual_wage'][1]:
                rpt['all']['max_annual_wage'] = [fips, wages]

            estab = int(fields[ANNUAL_AVG_ESTABS])
            rpt['all']['total_estab'] += estab
            if estab > rpt['all']['max_estab'][1]:
                rpt['all']['max_estab'] = [fips, estab]

            empl = int(fields[ANNUAL_AVG_EMPLVL])
            rpt['all']['total_empl'] += empl
            if empl > rpt['all']['max_empl'][1]:
                rpt['all']['max_empl'] = [fips, empl]

        elif fields[OWN_CODE] == '"5"' and fields[INDUSTRY_CODE] == '"5112"':
            rpt['soft']['num_areas'] += 1

            wages = int(fields[TOTAL_ANNUAL_WAGES])
            rpt['soft']['total_annual_wages'] += wages
            if wages > rpt['soft']['max_annual_wage'][1]:
                rpt['soft']['max_annual_wage'] = [fips, wages]

            estab = int(fields[ANNUAL_AVG_ESTABS])
            rpt['soft']['total_estab'] += estab
            if estab > rpt['soft']['max_estab'][1]:
                rpt['soft']['max_estab'] = [fips, estab]

            empl = int(fields[ANNUAL_AVG_EMPLVL])
            rpt['soft']['total_empl'] += empl
            if empl > rpt['soft']['max_empl'][1]:
                rpt['soft']['max_empl'] = [fips, empl]

# Translate the FIPS codes back into human-friendly strings
# I do this one time, at the end, instead of needlessly doing it many times in
# the middle.
rpt['all']['max_empl'][0] = areas[rpt['all']['max_empl'][0]]
rpt['all']['max_estab'][0] = areas[rpt['all']['max_estab'][0] ]
rpt['all']['max_annual_wage'][0] = areas[rpt['all']['max_annual_wage'][0]]
rpt['soft']['max_empl'][0] =  areas[rpt['soft']['max_empl'][0]]
rpt['soft']['max_estab'][0] =  areas[rpt['soft']['max_estab'][0]]
rpt['soft']['max_annual_wage'][0] =  areas[rpt['soft']['max_annual_wage'][0]]

after = time.time()  	  	  
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	  	  

## Print the completed report  	  	  
print_report(rpt)  	  	  
