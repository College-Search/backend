import csv
# UNITID
# INSTNM
# CITY
# STABBR
# ZIP
# INSTURL
# NPCURL
# MAIN
# NUMBRANCH
# PREDDEG
# HIGHDEG
# REGION
# LOCALE
# LOCALE2
# LATITUDE
# LONGITUDE
# HBCU
# PBI
# ANNHI
# TRIBAL
# AANAPII
# HSI
# NANTI
# MENONLY
# WOMENONLY
# RELAFFIL
# ADM_RATE
# ADM_RATE_ALL
# SATVR25
# SATVR75
# SATMT25
# SATMT75
# SATWR25
# SATWR75
# SATVRMID
# SATMTMID
# SATWRMID
# ACTCM25
# ACTCM75
# ACTEN25
# ACTEN75
# ACTMT25
# ACTMT75
# ACTWR25
# ACTWR75
# ACTCMMID
# ACTENMID
# ACTMTMID
# ACTWRMID
# SAT_AVG
# SAT_AVG_ALL
# STUFACR
# TUITIONFEE_IN
# TUITIONFEE_OUT
# TUITIONFEE_PROG

# Specify the columns to extract
columns = ["UNITID", "INSTNM", "CITY", "STABBR", "ZIP", "INSTURL", "NPCURL", "MAIN", "NUMBRANCH", "PREDDEG", "HIGHDEG", "REGION", "LOCALE", "LOCALE2", "LATITUDE", "LONGITUDE", "HBCU", "PBI", "ANNHI", "TRIBAL", "AANAPII", "HSI", "NANTI", "MENONLY", "WOMENONLY", "RELAFFIL", "ADM_RATE", "ADM_RATE_ALL", "SATVR25", "SATVR75", "SATMT25", "SATMT75", "SATWR25", "SATWR75", "SATVRMID", "SATMTMID", "SATWRMID", "ACTCM25", "ACTCM75", "ACTEN25", "ACTEN75", "ACTMT25", "ACTMT75", "ACTWR25", "ACTWR75", "ACTCMMID", "ACTENMID", "ACTMTMID", "ACTWRMID", "SAT_AVG", "SAT_AVG_ALL", "STUFACR", "TUITIONFEE_IN", "TUITIONFEE_OUT", "TUITIONFEE_PROG", "UGDS"]

# Open the input and output CSV files
with open("Most-Recent-Cohorts-Institution.csv", newline="") as input_file, open("filtered-college-data.csv", "w", newline="") as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=columns)
    
    # Write the header row to the output file
    writer.writeheader()
    
    # Iterate over each row in the input file, extract the specified columns, and write them to the output file
    for row in reader:
        if row["UGDS"] != "" and row["UGDS"] != "NULL" and float(row["UGDS"]) >= 1000:
            selected_row = {column: row[column] for column in columns}
            writer.writerow(selected_row)