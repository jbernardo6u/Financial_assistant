import requests
import pandas as pd

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    def get_financial_data(self, symbol, function):
        url = f'{self.base_url}?function={function}&symbol={symbol}&apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao obter dados financeiros: {response.status_code}")
    
    def get_cash_flow(self, symbol, start_year=None, end_year=None):
        data = self.get_financial_data(symbol, 'CASH_FLOW')
        annual_reports = data.get('annualReports', [])
        return self.filter_by_period(annual_reports, start_year, end_year)

    def get_income_statement(self, symbol, start_year=None, end_year=None):
        data = self.get_financial_data(symbol, 'INCOME_STATEMENT')
        annual_reports = data.get('annualReports', [])
        return self.filter_by_period(annual_reports, start_year, end_year)

    def get_balance_sheet(self, symbol, start_year=None, end_year=None):
        data = self.get_financial_data(symbol, 'BALANCE_SHEET')
        annual_reports = data.get('annualReports', [])
        return self.filter_by_period(annual_reports, start_year, end_year)

    def filter_by_period(self, reports, start_year=None, end_year=None):
        filtered_reports = []
        for report in reports:
            year = int(report['fiscalDateEnding'][:4])
            if (start_year is None or year >= start_year) and (end_year is None or year <= end_year):
                filtered_reports.append(report)
        return filtered_reports
    
    def get_gross_profit(self, symbol, start_year=None, end_year=None):
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        gross_profits = []
        for report in income_statements:
            gross_profit = float(report['grossProfit'])
            gross_profits.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'grossProfit': gross_profit
            })
        return gross_profits
    
    def get_gross_profit_margin(self, symbol, start_year=None, end_year=None):
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        profit_margins = []
        for report in income_statements:
            gross_profit = float(report['grossProfit'])
            revenue = float(report['totalRevenue'])
            gross_profit_margin = (gross_profit / revenue) * 100
            profit_margins.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'grossProfit': gross_profit,
                'revenue': revenue,
                'grossProfitMargin': gross_profit_margin
            })
        return profit_margins
    
    def get_operating_profit(self, symbol, start_year=None, end_year=None):
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        operating_profits = []
        for report in income_statements:
            gross_profit = float(report['grossProfit'])
            operating_expenses = float(report.get('operatingExpenses', 0))  # Pode não estar presente em todos os relatórios
            r_d_costs = float(report.get('researchAndDevelopment', 0))  # Pode não estar presente em todos os relatórios
            
            operating_profit = gross_profit - operating_expenses - r_d_costs
            operating_profits.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'grossProfit': gross_profit,
                'operatingExpenses': operating_expenses,
                'r_d_costs': r_d_costs,
                'operatingProfit': operating_profit
            })
        return operating_profits
    
    def get_operating_profit_margin(self, symbol, start_year=None, end_year=None):
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        profit_margins = []
        for report in income_statements:
            gross_profit = float(report['grossProfit'])
            operating_expenses = float(report.get('operatingExpenses', 0))
            r_d_costs = float(report.get('researchAndDevelopment', 0))
            
            operating_profit = gross_profit - operating_expenses - r_d_costs
            operating_profit_margin = (operating_profit / gross_profit) * 100 if gross_profit != 0 else 0
            
            profit_margins.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'grossProfit': gross_profit,
                'operatingExpenses': operating_expenses,
                'r_d_costs': r_d_costs,
                'operatingProfit': operating_profit,
                'operatingProfitMargin': operating_profit_margin
            })
        return profit_margins
    
    def get_net_profit_margin(self, symbol, start_year=None, end_year=None):
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        profit_margins = []
        for report in income_statements:
            net_profit = float(report['netIncome'])
            revenue = float(report['totalRevenue'])
            
            net_profit_margin = (net_profit / revenue) * 100 if revenue != 0 else 0
            
            profit_margins.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'netProfit': net_profit,
                'revenue': revenue,
                'netProfitMargin': net_profit_margin
            })
        return profit_margins

    #Nota: get_profit_growth_rate-> apresenta alguns valores negativos
    def get_profit_growth_rate(self, symbol, start_year=None, end_year=None):
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        growth_rates = []
        
        for i in range(1, len(income_statements)):  # Começa do segundo relatório
            current_report = income_statements[i]
            previous_report = income_statements[i - 1]
            
            current_profit = float(current_report['netIncome'])
            previous_profit = float(previous_report['netIncome'])
            
            if previous_profit != 0:
                profit_growth_rate = ((current_profit - previous_profit) / previous_profit) * 100
            else:
                profit_growth_rate = 0  # Evita divisão por zero
            
            growth_rates.append({
                'fiscalDateEnding': current_report['fiscalDateEnding'],
                'currentProfit': current_profit,
                'previousProfit': previous_profit,
                'profitGrowthRate': profit_growth_rate
            })
        
        return growth_rates
    

    def get_eps(self, symbol, start_year=None, end_year=None):
        # Obter a visão geral da empresa
        overview = self.get_financial_data(symbol, 'OVERVIEW')
        outstanding_shares = float(overview.get('SharesOutstanding', 0))  # Ações em circulação
        income_statements = self.get_income_statement(symbol, start_year, end_year)
        eps_list = []
        for report in income_statements:
            net_profit = float(report['netIncome'])
            if outstanding_shares > 0:
                eps = net_profit / outstanding_shares
            else:
                eps = 0  # Evita divisão por zero
            eps_list.append({
            'symbol': symbol,
            'netProfit': net_profit,
            'outstandingShares': outstanding_shares,
            'EPS': eps
        })
        
        return eps_list
    
    def get_debt_ratio(self, symbol, start_year=None, end_year=None):
        balance_sheets = self.get_balance_sheet(symbol, start_year, end_year)
        debt_ratios = []
        for report in balance_sheets:
            total_liabilities = float(report['totalLiabilities'])
            shareholders_equity = float(report['totalShareholderEquity'])
            if shareholders_equity != 0:
                debt_ratio = total_liabilities / shareholders_equity
            else:
                debt_ratio = 0  # Evita divisão por zero
            debt_ratios.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'totalLiabilities': total_liabilities,
                'shareholdersEquity': shareholders_equity,
                'debtRatio': debt_ratio
            })
        return debt_ratios
    
    
    def get_current_ratio(self, symbol, start_year=None, end_year=None):
        balance_sheets = self.get_balance_sheet(symbol, start_year, end_year)
        current_ratios = []
        for report in balance_sheets:
            current_assets = float(report.get('totalCurrentAssets', 0))
            current_liabilities = float(report.get('totalCurrentLiabilities', 0))
            if current_liabilities != 0:
                current_ratio = current_assets / current_liabilities
            else:
                current_ratio = 0  # Evita divisão por zero
            current_ratios.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'currentAssets': current_assets,
                'currentLiabilities': current_liabilities,
                'currentRatio': current_ratio
            })
        return current_ratios
    
    
    def get_cash_ratio(self, symbol, start_year=None, end_year=None):
        balance_sheets = self.get_balance_sheet(symbol, start_year, end_year)
        cash_ratios = []
        for report in balance_sheets:
            cash_and_equivalents = float(report.get('cashAndCashEquivalentsAtCarryingValue', 0))
            total_assets = float(report.get('totalAssets', 0))
            if total_assets != 0:
                cash_ratio = cash_and_equivalents / total_assets
            else:
                cash_ratio = 0  # Evita divisão por zero
            cash_ratios.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'cashAndEquivalents': cash_and_equivalents,
                'totalAssets': total_assets,
                'cashRatio': cash_ratio
            })
        return cash_ratios

    def get_operating_cash_flow(self, symbol, start_year=None, end_year=None):
        cash_flows = self.get_cash_flow(symbol, start_year, end_year)
        operating_cash_flows = []
        for report in cash_flows:
            cash_generated_by_operating_activities = float(report.get('operatingCashflow', 0))
            operating_cash_flows.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'operatingCashFlow': cash_generated_by_operating_activities
            })
        return operating_cash_flows


    def get_free_cash_flow(self, symbol, start_year=None, end_year=None):
        cash_flows = self.get_cash_flow(symbol, start_year, end_year)
        free_cash_flows = []
        for report in cash_flows:
            operating_cash_flow = float(report.get('operatingCashflow', 0))
            capital_expenditure = float(report.get('capitalExpenditures', 0))
            free_cash_flow = operating_cash_flow - capital_expenditure
            free_cash_flows.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'operatingCashFlow': operating_cash_flow,
                'capitalExpenditure': capital_expenditure,
                'freeCashFlow': free_cash_flow
            })
        return free_cash_flows
    
    def get_capex_ratio(self, symbol, start_year=None, end_year=None):
        cash_flows = self.get_cash_flow(symbol, start_year, end_year)
        capex_ratios = []
        for report in cash_flows:
            operating_cash_flow = float(report.get('operatingCashflow', 0))
            capital_expenditure = float(report.get('capitalExpenditures', 0))
            if operating_cash_flow != 0:
                capex_ratio = capital_expenditure / operating_cash_flow
            else:
                capex_ratio = 0  # Evita divisão por zero
            capex_ratios.append({
                'fiscalDateEnding': report['fiscalDateEnding'],
                'operatingCashFlow': operating_cash_flow,
                'capitalExpenditure': capital_expenditure,
                'capexRatio': capex_ratio
            })
        return capex_ratios





# Função principal
if __name__ == '__main__':
    API_KEY = 'my_alpha_vantage_api_key'
    symbols = ['MSFT'] # Lista de empresas
    # symbols = ['AAPL', 'GOOGL', 'MSFT']

    # Instancia da classe com a chave de API
    alpha_api = AlphaVantageAPI(API_KEY)

    for symbol in symbols:
        print(f"Obtendo dados para: {symbol}")
        
        """ # Cash Flow da empresa
        cash_flow_data = alpha_api.get_cash_flow(symbol)
        income_statement_data = alpha_api.get_income_statement(symbol)
        balance_sheet_data = alpha_api.get_balance_sheet(symbol)

        # Converte os dados em DataFrames
        df_cash_flow = pd.DataFrame(cash_flow_data)
        df_income_statement = pd.DataFrame(income_statement_data)
        df_balance_sheet = pd.DataFrame(balance_sheet_data) """
        
        # Salvar os dados em arquivos Excel separados para cada empresa
        """ df_cash_flow.to_excel(f'{symbol}_cash_flow_data.xlsx', index=False)
        df_income_statement.to_excel(f'{symbol}_income_statement_data.xlsx', index=False)
        df_balance_sheet.to_excel(f'{symbol}_balance_sheet_data.xlsx', index=False) """
        
        """ # Obter o Cash Flow do período entre 2019 e 2021
        cash_flow_data_period = alpha_api.get_cash_flow(symbol, start_year=2019, end_year=2021)
        
        # Obter o Balance Sheet entre 2018 e 2020
        balance_sheet_data_period = alpha_api.get_balance_sheet(symbol, start_year=2018, end_year=2020)
        
        # Obter o Income Statement entre 2018 e 2020
        income_statement_data_period = alpha_api.get_income_statement(symbol, start_year=2018, end_year=2020)
        
        # Converte os dados de período em DataFrames
        df_cash_flow_period = pd.DataFrame(cash_flow_data_period)
        df_balance_sheet_period = pd.DataFrame(balance_sheet_data_period)
        df_income_statement_period = pd.DataFrame(income_statement_data_period) """

        # Salvar os dados de períodos específicos em arquivos Excel separados para cada empresa
        """  df_cash_flow_period.to_excel(f'{symbol}_cash_flow_data_2019_2021.xlsx', index=False)
        df_balance_sheet_period.to_excel(f'{symbol}_balance_sheet_data_2018_2020.xlsx', index=False)
        df_income_statement_period.to_excel(f'{symbol}_income_statement_data_2018_2020.xlsx', index=False) """
        get_eps = alpha_api.get_eps(symbol, start_year=2022, end_year=2024)
        print(get_eps)
    
    # get_financial_data = alpha_api.get_financial_data(symbol, 'OVERVIEW')
    # print(get_financial_data)
