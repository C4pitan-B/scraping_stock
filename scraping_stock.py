
import requests
from bs4 import BeautifulSoup
import gzip
from io import BytesIO

def scraping (tikers):
 
  url = "https://finviz.com/quote.ashx?t="+tikers+"&ty=c&p=d&b=1"

  # Users headers
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

  # Make dictionary for data storage
  data_dict = {"Stock": tikers}

  # Realiza una solicitud HTTP GET a la página
  response = requests.get(url, headers=headers)

  # Checks if the request was successful (status code 200)
  if response.status_code == 200:
      # Gzip compression verification
        if 'Content-Encoding' in response.headers and response.headers['Content-Encoding'] == 'gzip':
            try:
               compressed_content = BytesIO(response.content)
               decompressed_content = gzip.GzipFile(fileobj=compressed_content)
               content = decompressed_content.read()
            except gzip.BadGzipFile:
               # decompression failure
                content = response.text
        else:
           # If web site dont use Gzip
            content = response.text

        # Analyze page content with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        #Find and traverse the table with the "tr" that have the class "table-dark-row"
        table = soup.find('table', class_='snapshot-table2')   
        
        for row in table.find_all('tr', class_='table-dark-row'):
            cells = row.find_all('td')
            if len(cells) >= 2:
              # Take odd column as key and even column as value
                for i in range(0, len(cells), 2):
                  key = cells[i].text.strip()
                  value = cells[i + 1].text.strip()
                  # make up the dictionary
                  data_dict[key] = value
                          
        return data_dict
  else:
        print("Error getting page:", response.status_code)

  