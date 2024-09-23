import yfinance as yf
import pandas as pd
from config import API_KEY, SOCIETY



society = SOCIETY
company = yf.Ticker(society)

class IncomeStatementIndicators:
    def __init__(self) -> None:
        self.income_statement_rapport = company.income_stmt.T
    def show_rapport(self):
        print(self.income_statement_rapport.items)
    

class BalanceSheetIndicators:
    def __init__(self) -> None:
        self.balance_sheet_rapport = company.balance_sheet

    def show_rapport(self):    
        print(self.balance_sheet_rapport.items)

class CashFlow:
    def __init__(self) -> None:
        self.cash_flow_rapport = company.balance_sheet

    def show_rapport(self):
        print(self.cash_flow_rapport.items)