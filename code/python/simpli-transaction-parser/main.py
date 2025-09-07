from bs4 import BeautifulSoup
from datetime import datetime

# Read Index
with open("index.html") as f:
    index = f.read()

print(index)


# Parse Index
soup = BeautifulSoup(index, 'html.parser')

with open('transactions.qfx', 'w') as qfxfile: 
    # Write the header for the QFX file
    qfxfile.write('OFXHEADER:100\nDATA:OFXSGML\nVERSION:102\nSECURITY:NONE\nENCODING:USASCII\nCHARSET:1252\nCOMPRESSION:NONE\nOLDFILEUID:NONE\nNEWFILEUID:NONE\n\n<OFX>\n<BANKMSGSRSV1>\n<STMTTRNRS>\n<STMTRS>\n<BANKTRANLIST>\n')

    for row in soup.find_all('tr', class_='transaction-row'):
        date_str = row.find('td', class_='date').text.strip()
        date_object = datetime.strptime(date_str, "%b %d, %Y")

        description = row.find('span', class_='transactionDescription').text.strip()
        debit = row.find('td', class_='debit').find('span').text.strip()
        balance = row.find('td', class_='balance').find('span').text.strip()
        
        # date object to string with format %Y%m%d%H%M%S[%z:%Z]
        dateFmt = date_object.strftime('%Y%m%d%H%M%S')+'[0:GMT]'

        # OFX transaction type:
        # if row['payee'] == 'Chase': 
        #     txType = 'TRANSFER' 
        # elif row['type'] == 'Payment': 
        #     txType = 'CREDIT'
        # else:
        txType = 'DEBIT'

        # skip transfers in output file for now
        if txType != 'TRANSFER':
            qfxfile.write(f'<STMTTRN>\n<DTPOSTED>{dateFmt}</DTPOSTED>\n<TRNTYPE>{txType}<TRNTYPE>\n<FITID>{row["transaction_id"]}</FITID>\n<NAME>{row["payer"]}</NAME>\n<MEMO>gross:{row["amount"]} fees:{row["fees"]} {row["status"]} {row["transaction_id"]}</MEMO>\n<TRNAMT>{row["net"]}</TRNAMT>\n<REFNUM>{row["payer"]}</REFNUM>\n</STMTTRN>\n')
            
    # Write the footer for the QFX file
    qfxfile.write('</BANKTRANLIST>\n</STMTRS>\n</STMTTRNRS>\n</BANKMSGSRSV1>\n</OFX>')