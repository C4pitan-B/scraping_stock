# scraping_stock
 scraping url finviz

The objective of this function is to obtain the data associated with a certain stock, scraping "finviz.com".
All this data is public, we only seek to automate the action.

This function requires the stock ticker as a parameter. After scraping it will return the data as a dictionary [ ].
For example:
{'Stock': 'AMZN', 'Index': 'NDX, S&P 500',.........
...................'SMA200': '11.87%', 'Volume': '66,092,795', 'Change': '0.00%'}

You can invoke this function from your main program and then work with them through the [data_dict] dictionary. [ your_dict = scraping_stock.scraping("AMZN") ]

In the event that there is an error opening the web page, the error code will be reported in the console using "print".

I hope it's useful!