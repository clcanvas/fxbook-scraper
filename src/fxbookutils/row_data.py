from bs4 import BeautifulSoup

class calRow:
    def __init__(self, day, time, name, dataRowID, impact, symbol, previous_value, concensus, actual):
        self.day = day
        self.time = time
        self.name = name
        self.dataRowID = dataRowID
        self.impact = impact
        self.symbol = symbol
        self.previous_value = previous_value
        self.concensus = concensus
        self.actual = actual

    def __str__(self):
        return f"{self.day.strip()} {self.time.strip()} | {self.symbol.strip()}, {self.name.strip()}, {self.impact.strip()}, {str(self.previous_value).strip()}, {str(self.concensus).strip()}, {str(self.actual).strip()}"

def getRows(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    tr_tags = soup.find_all('tr')
    econCalRows = []
    
    for tr in tr_tags:
        data_row_id = tr.get('data-row-id')
        td_tags = tr.find_all('td')
        if data_row_id:     
            row = defineRow(td_tags, data_row_id)
            econCalRows.append(row)
    return econCalRows

def defineRow(td_tags, data_row_id):
    impact = td_tags[5].find('div').text
    currentRow = calRow(None, None, None, None, None, "SYM", None, None, None)
    currentRow.symbol = td_tags[3].text
    date = td_tags[0].find('div').text
    if date:   
        currentRow.day = date.strip()[0:6]
        currentRow.time = date.strip()[8:13]
    if impact:
        currentRow.impact = impact
    currentRow.dataRowID = data_row_id
    for td in td_tags:
        name = td.find('a')
        if name: # Get the name of the row
            month = td.find('span') # only look for rows with month on the end, e.g. xyx (Apr)
            if month: # if its found
                currentRow.name = f"{name.text} {month.text}" # edit attributes of current row
        span_tags = td.find_all('span')
        previous_value = td.get('previous-value')
        actual = td.get('data-actual')
        for span in span_tags: # this is for previous and actual values
            if previous_value:
                currentRow.previous_value = span.text
            elif actual:
                text = span.text
                if text.strip() == "":
                    currentRow.actual = "None"
                else:
                    currentRow.actual = span.text
                break
        consensus = td.get('concensus')
        if consensus: # for the consensus value
            div_tags = td.find_all('div')
            for div in div_tags:
                currentRow.concensus = div.text
                break
    return currentRow