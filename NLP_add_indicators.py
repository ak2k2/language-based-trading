from openai_api_request import make_openai_request
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_ta as ta
import numpy as np
import plotly.graph_objects as go
import plotly.express as px



o_api = make_openai_request()

ticker = input("Enter a ticker supported by yfinance: ")
interval = '1d'
daily_data = yf.download(ticker,'2015-12-01','2023-01-24', interval=interval)

#if daily data has any nan values, drop the entire row
daily_data['hlc3'] = (daily_data['High'] + daily_data['Low'] + daily_data['Close']) / 3


# ask to summon indicators
def add_indicator(dataframe):
    indicator = input("Describe an indicator you would like to see:")
    ind1 = o_api.request("Pandas code to add a column named " + indicator + " to 'dataframe'. Dataframe already exists and has four columns, 'Open', 'High', 'Low', and 'Close.")
    print(ind1)
    exec(ind1)
    return dataframe

def add_long_short_column(dataframe):
    input_condition = input("Go Long When: ") # example: "Go Long When: MACD > 0"
    added_LS = o_api.request("Pandas code to add a column named 'Long_Signal' to 'dataframe'. dataframe['Long_Signal'] should be 1 when " + input_condition  + " and 0 otherwise.")
    print(added_LS)
    exec(added_LS)
    return dataframe


added_1ind = add_indicator(daily_data)
added_2ind = add_indicator(added_1ind)
added_3ind = add_indicator(added_2ind)
added_LS = add_long_short_column(added_3ind)


final_plot = added_3ind.drop(["Volume", "Open", "High", "Low", "Close", "Adj Close",], axis=1)

fig = px.line(final_plot, x=final_plot.index, y=final_plot.columns)
fig.show()
