# Trading Signal Visualization
[HTML demo of summoning an AVWAP indicator](https://htmlpreview.github.io/?https://github.com/ak2k2/ChartCraft/blob/main/AAVWAP.html)

This program allows users to visualize trading signals using Plotly charts. It uses yfinance to download historical data, OpenAI's GPT-3 NLP to summon indicators, and Plotly to visualize the data.

## Prerequisites

In order to run this program, you must have the following installed:

- Python 3
- yfinance
- OpenAI's GPT-3 NLP
- Plotly

## Usage

To use this program, simply run it on the command line. You will be prompted to enter a ticker supported by yfinance. The program will then download historical data, summon indicators, and visualize the data with Plotly charts.

## Example

Let's say we want to create a trading signal for Apple (AAPL). We run the program and enter AAPL as our ticker. The program will then download the historical data, summon indicators, and visualize the data with Plotly charts.

We can then add our own indicators, such as MACD, RSI, and Moving Average, to create a trading signal. We can also add a "Long Signal" column which will be 1 when the conditions we specify are met, and 0 otherwise.

Once we have added all the indicators and a long signal column, the program will generate a Plotly chart showing the historical data and the indicators we added. This chart can be used to analyze the trading signal and visualize precise historical returns.
