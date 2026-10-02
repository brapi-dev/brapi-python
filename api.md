# Quote

Types:

```python
from brapi.types import (
    BalanceSheetEntry,
    DividendsData,
    FinancialDataEntry,
    QuoteRetrieveResponse,
    QuoteListResponse,
)
```

Methods:

- <code title="get /api/quote/{tickers}">client.quote.<a href="./src/brapi/resources/quote.py">retrieve</a>(tickers, \*\*<a href="src/brapi/types/quote_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/quote_retrieve_response.py">QuoteRetrieveResponse</a></code>
- <code title="get /api/quote/list">client.quote.<a href="./src/brapi/resources/quote.py">list</a>(\*\*<a href="src/brapi/types/quote_list_params.py">params</a>) -> <a href="./src/brapi/types/quote_list_response.py">QuoteListResponse</a></code>

# Available

Types:

```python
from brapi.types import AvailableListResponse
```

Methods:

- <code title="get /api/available">client.available.<a href="./src/brapi/resources/available.py">list</a>(\*\*<a href="src/brapi/types/available_list_params.py">params</a>) -> <a href="./src/brapi/types/available_list_response.py">AvailableListResponse</a></code>

# V2

## Crypto

Types:

```python
from brapi.types.v2 import CryptoRetrieveResponse, CryptoListAvailableResponse
```

Methods:

- <code title="get /api/v2/crypto">client.v2.crypto.<a href="./src/brapi/resources/v2/crypto.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/crypto_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/crypto_retrieve_response.py">CryptoRetrieveResponse</a></code>
- <code title="get /api/v2/crypto/available">client.v2.crypto.<a href="./src/brapi/resources/v2/crypto.py">list_available</a>(\*\*<a href="src/brapi/types/v2/crypto_list_available_params.py">params</a>) -> <a href="./src/brapi/types/v2/crypto_list_available_response.py">CryptoListAvailableResponse</a></code>

## Currency

Types:

```python
from brapi.types.v2 import (
    CurrencyRetrieveResponse,
    CurrencyHistoricalResponse,
    CurrencyListAvailableResponse,
)
```

Methods:

- <code title="get /api/v2/currency">client.v2.currency.<a href="./src/brapi/resources/v2/currency.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/currency_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/currency_retrieve_response.py">CurrencyRetrieveResponse</a></code>
- <code title="get /api/v2/currency/historical">client.v2.currency.<a href="./src/brapi/resources/v2/currency.py">historical</a>(\*\*<a href="src/brapi/types/v2/currency_historical_params.py">params</a>) -> <a href="./src/brapi/types/v2/currency_historical_response.py">CurrencyHistoricalResponse</a></code>
- <code title="get /api/v2/currency/available">client.v2.currency.<a href="./src/brapi/resources/v2/currency.py">list_available</a>(\*\*<a href="src/brapi/types/v2/currency_list_available_params.py">params</a>) -> <a href="./src/brapi/types/v2/currency_list_available_response.py">CurrencyListAvailableResponse</a></code>

## Inflation

Types:

```python
from brapi.types.v2 import InflationRetrieveResponse, InflationListAvailableResponse
```

Methods:

- <code title="get /api/v2/inflation">client.v2.inflation.<a href="./src/brapi/resources/v2/inflation.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/inflation_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/inflation_retrieve_response.py">InflationRetrieveResponse</a></code>
- <code title="get /api/v2/inflation/available">client.v2.inflation.<a href="./src/brapi/resources/v2/inflation.py">list_available</a>(\*\*<a href="src/brapi/types/v2/inflation_list_available_params.py">params</a>) -> <a href="./src/brapi/types/v2/inflation_list_available_response.py">InflationListAvailableResponse</a></code>

## PrimeRate

Types:

```python
from brapi.types.v2 import PrimeRateRetrieveResponse, PrimeRateListAvailableResponse
```

Methods:

- <code title="get /api/v2/prime-rate">client.v2.prime_rate.<a href="./src/brapi/resources/v2/prime_rate.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/prime_rate_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/prime_rate_retrieve_response.py">PrimeRateRetrieveResponse</a></code>
- <code title="get /api/v2/prime-rate/available">client.v2.prime_rate.<a href="./src/brapi/resources/v2/prime_rate.py">list_available</a>(\*\*<a href="src/brapi/types/v2/prime_rate_list_available_params.py">params</a>) -> <a href="./src/brapi/types/v2/prime_rate_list_available_response.py">PrimeRateListAvailableResponse</a></code>

## Dictionary

Types:

```python
from brapi.types.v2 import DictionaryRetrieveResponse
```

Methods:

- <code title="get /api/v2/dictionary">client.v2.dictionary.<a href="./src/brapi/resources/v2/dictionary.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/dictionary_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/dictionary_retrieve_response.py">DictionaryRetrieveResponse</a></code>

## Stocks

Types:

```python
from brapi.types.v2 import (
    StockFundamentalsSeries,
    StockBalanceSheetResponse,
    StockCashFlowResponse,
    StockDividendsResponse,
    StockFinancialDataResponse,
    StockHistoricalResponse,
    StockIncomeStatementResponse,
    StockInsiderTransactionsResponse,
    StockProfileResponse,
    StockQuoteResponse,
    StockStatisticsResponse,
    StockValueAddedResponse,
)
```

Methods:

- <code title="get /api/v2/stocks/balance-sheet">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">balance_sheet</a>(\*\*<a href="src/brapi/types/v2/stock_balance_sheet_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_balance_sheet_response.py">StockBalanceSheetResponse</a></code>
- <code title="get /api/v2/stocks/cash-flow">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">cash_flow</a>(\*\*<a href="src/brapi/types/v2/stock_cash_flow_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_cash_flow_response.py">StockCashFlowResponse</a></code>
- <code title="get /api/v2/stocks/dividends">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">dividends</a>(\*\*<a href="src/brapi/types/v2/stock_dividends_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_dividends_response.py">StockDividendsResponse</a></code>
- <code title="get /api/v2/stocks/financial-data">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">financial_data</a>(\*\*<a href="src/brapi/types/v2/stock_financial_data_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_financial_data_response.py">StockFinancialDataResponse</a></code>
- <code title="get /api/v2/stocks/historical">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">historical</a>(\*\*<a href="src/brapi/types/v2/stock_historical_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_historical_response.py">StockHistoricalResponse</a></code>
- <code title="get /api/v2/stocks/income-statement">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">income_statement</a>(\*\*<a href="src/brapi/types/v2/stock_income_statement_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_income_statement_response.py">StockIncomeStatementResponse</a></code>
- <code title="get /api/v2/stocks/insider-transactions">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">insider_transactions</a>(\*\*<a href="src/brapi/types/v2/stock_insider_transactions_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_insider_transactions_response.py">StockInsiderTransactionsResponse</a></code>
- <code title="get /api/v2/stocks/profile">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">profile</a>(\*\*<a href="src/brapi/types/v2/stock_profile_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_profile_response.py">StockProfileResponse</a></code>
- <code title="get /api/v2/stocks/quote">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">quote</a>(\*\*<a href="src/brapi/types/v2/stock_quote_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_quote_response.py">StockQuoteResponse</a></code>
- <code title="get /api/v2/stocks/statistics">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">statistics</a>(\*\*<a href="src/brapi/types/v2/stock_statistics_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_statistics_response.py">StockStatisticsResponse</a></code>
- <code title="get /api/v2/stocks/value-added">client.v2.stocks.<a href="./src/brapi/resources/v2/stocks.py">value_added</a>(\*\*<a href="src/brapi/types/v2/stock_value_added_params.py">params</a>) -> <a href="./src/brapi/types/v2/stock_value_added_response.py">StockValueAddedResponse</a></code>

## Tickers

Types:

```python
from brapi.types.v2 import (
    TickerListResponse,
    TickerCoverageResponse,
    TickerRenamesResponse,
    TickerResolveResponse,
)
```

Methods:

- <code title="get /api/v2/tickers">client.v2.tickers.<a href="./src/brapi/resources/v2/tickers.py">list</a>(\*\*<a href="src/brapi/types/v2/ticker_list_params.py">params</a>) -> <a href="./src/brapi/types/v2/ticker_list_response.py">TickerListResponse</a></code>
- <code title="get /api/v2/tickers/coverage">client.v2.tickers.<a href="./src/brapi/resources/v2/tickers.py">coverage</a>(\*\*<a href="src/brapi/types/v2/ticker_coverage_params.py">params</a>) -> <a href="./src/brapi/types/v2/ticker_coverage_response.py">TickerCoverageResponse</a></code>
- <code title="get /api/v2/tickers/renames">client.v2.tickers.<a href="./src/brapi/resources/v2/tickers.py">renames</a>(\*\*<a href="src/brapi/types/v2/ticker_renames_params.py">params</a>) -> <a href="./src/brapi/types/v2/ticker_renames_response.py">TickerRenamesResponse</a></code>
- <code title="get /api/v2/tickers/resolve">client.v2.tickers.<a href="./src/brapi/resources/v2/tickers.py">resolve</a>(\*\*<a href="src/brapi/types/v2/ticker_resolve_params.py">params</a>) -> <a href="./src/brapi/types/v2/ticker_resolve_response.py">TickerResolveResponse</a></code>

## Fii

Types:

```python
from brapi.types.v2 import (
    PaginationMeta,
    FiiListResponse,
    FiiAnnualReportsResponse,
    FiiDividendsResponse,
    FiiFinancialsResponse,
    FiiHistoricalResponse,
    FiiReportsResponse,
)
```

Methods:

- <code title="get /api/v2/fii/list">client.v2.fii.<a href="./src/brapi/resources/v2/fii/fii.py">list</a>(\*\*<a href="src/brapi/types/v2/fii_list_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii_list_response.py">FiiListResponse</a></code>
- <code title="get /api/v2/fii/annual-reports">client.v2.fii.<a href="./src/brapi/resources/v2/fii/fii.py">annual_reports</a>(\*\*<a href="src/brapi/types/v2/fii_annual_reports_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii_annual_reports_response.py">FiiAnnualReportsResponse</a></code>
- <code title="get /api/v2/fii/dividends">client.v2.fii.<a href="./src/brapi/resources/v2/fii/fii.py">dividends</a>(\*\*<a href="src/brapi/types/v2/fii_dividends_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii_dividends_response.py">FiiDividendsResponse</a></code>
- <code title="get /api/v2/fii/financials">client.v2.fii.<a href="./src/brapi/resources/v2/fii/fii.py">financials</a>(\*\*<a href="src/brapi/types/v2/fii_financials_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii_financials_response.py">FiiFinancialsResponse</a></code>
- <code title="get /api/v2/fii/historical">client.v2.fii.<a href="./src/brapi/resources/v2/fii/fii.py">historical</a>(\*\*<a href="src/brapi/types/v2/fii_historical_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii_historical_response.py">FiiHistoricalResponse</a></code>
- <code title="get /api/v2/fii/reports">client.v2.fii.<a href="./src/brapi/resources/v2/fii/fii.py">reports</a>(\*\*<a href="src/brapi/types/v2/fii_reports_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii_reports_response.py">FiiReportsResponse</a></code>

### Indicators

Types:

```python
from brapi.types.v2.fii import IndicatorRetrieveResponse, IndicatorHistoryResponse
```

Methods:

- <code title="get /api/v2/fii/indicators">client.v2.fii.indicators.<a href="./src/brapi/resources/v2/fii/indicators.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/fii/indicator_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii/indicator_retrieve_response.py">IndicatorRetrieveResponse</a></code>
- <code title="get /api/v2/fii/indicators/history">client.v2.fii.indicators.<a href="./src/brapi/resources/v2/fii/indicators.py">history</a>(\*\*<a href="src/brapi/types/v2/fii/indicator_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii/indicator_history_response.py">IndicatorHistoryResponse</a></code>

### Portfolio

Types:

```python
from brapi.types.v2.fii import (
    FiiFinancialAsset,
    FiiPortfolioAllocation,
    FiiPortfolioSummary,
    FiiProperty,
    PortfolioRetrieveResponse,
    PortfolioHistoryResponse,
)
```

Methods:

- <code title="get /api/v2/fii/portfolio">client.v2.fii.portfolio.<a href="./src/brapi/resources/v2/fii/portfolio.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/fii/portfolio_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii/portfolio_retrieve_response.py">PortfolioRetrieveResponse</a></code>
- <code title="get /api/v2/fii/portfolio/history">client.v2.fii.portfolio.<a href="./src/brapi/resources/v2/fii/portfolio.py">history</a>(\*\*<a href="src/brapi/types/v2/fii/portfolio_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii/portfolio_history_response.py">PortfolioHistoryResponse</a></code>

### Properties

Types:

```python
from brapi.types.v2.fii import FiiPropertySummary, PropertyRetrieveResponse, PropertyHistoryResponse
```

Methods:

- <code title="get /api/v2/fii/properties">client.v2.fii.properties.<a href="./src/brapi/resources/v2/fii/properties.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/fii/property_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii/property_retrieve_response.py">PropertyRetrieveResponse</a></code>
- <code title="get /api/v2/fii/properties/history">client.v2.fii.properties.<a href="./src/brapi/resources/v2/fii/properties.py">history</a>(\*\*<a href="src/brapi/types/v2/fii/property_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/fii/property_history_response.py">PropertyHistoryResponse</a></code>

## Funds

Types:

```python
from brapi.types.v2 import (
    FundHolding,
    FundPaginationMeta,
    FundListResponse,
    FundDividendsResponse,
    FundIndicatorsResponse,
    FundPortfolioResponse,
    FundProfileResponse,
)
```

Methods:

- <code title="get /api/v2/funds/list">client.v2.funds.<a href="./src/brapi/resources/v2/funds/funds.py">list</a>(\*\*<a href="src/brapi/types/v2/fund_list_params.py">params</a>) -> <a href="./src/brapi/types/v2/fund_list_response.py">FundListResponse</a></code>
- <code title="get /api/v2/funds/dividends">client.v2.funds.<a href="./src/brapi/resources/v2/funds/funds.py">dividends</a>(\*\*<a href="src/brapi/types/v2/fund_dividends_params.py">params</a>) -> <a href="./src/brapi/types/v2/fund_dividends_response.py">FundDividendsResponse</a></code>
- <code title="get /api/v2/funds/indicators">client.v2.funds.<a href="./src/brapi/resources/v2/funds/funds.py">indicators</a>(\*\*<a href="src/brapi/types/v2/fund_indicators_params.py">params</a>) -> <a href="./src/brapi/types/v2/fund_indicators_response.py">FundIndicatorsResponse</a></code>
- <code title="get /api/v2/funds/portfolio">client.v2.funds.<a href="./src/brapi/resources/v2/funds/funds.py">portfolio</a>(\*\*<a href="src/brapi/types/v2/fund_portfolio_params.py">params</a>) -> <a href="./src/brapi/types/v2/fund_portfolio_response.py">FundPortfolioResponse</a></code>
- <code title="get /api/v2/funds/profile">client.v2.funds.<a href="./src/brapi/resources/v2/funds/funds.py">profile</a>(\*\*<a href="src/brapi/types/v2/fund_profile_params.py">params</a>) -> <a href="./src/brapi/types/v2/fund_profile_response.py">FundProfileResponse</a></code>

### Nav

Types:

```python
from brapi.types.v2.funds import NavHistoryResponse
```

Methods:

- <code title="get /api/v2/funds/nav/history">client.v2.funds.nav.<a href="./src/brapi/resources/v2/funds/nav.py">history</a>(\*\*<a href="src/brapi/types/v2/funds/nav_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/funds/nav_history_response.py">NavHistoryResponse</a></code>

### Fiagro

Types:

```python
from brapi.types.v2.funds import FiagroPortfolioResponse, FiagroReportsResponse
```

Methods:

- <code title="get /api/v2/funds/fiagro/portfolio">client.v2.funds.fiagro.<a href="./src/brapi/resources/v2/funds/fiagro.py">portfolio</a>(\*\*<a href="src/brapi/types/v2/funds/fiagro_portfolio_params.py">params</a>) -> <a href="./src/brapi/types/v2/funds/fiagro_portfolio_response.py">FiagroPortfolioResponse</a></code>
- <code title="get /api/v2/funds/fiagro/reports">client.v2.funds.fiagro.<a href="./src/brapi/resources/v2/funds/fiagro.py">reports</a>(\*\*<a href="src/brapi/types/v2/funds/fiagro_reports_params.py">params</a>) -> <a href="./src/brapi/types/v2/funds/fiagro_reports_response.py">FiagroReportsResponse</a></code>

### Fidc

Types:

```python
from brapi.types.v2.funds import FidcPortfolioResponse, FidcReportsResponse
```

Methods:

- <code title="get /api/v2/funds/fidc/portfolio">client.v2.funds.fidc.<a href="./src/brapi/resources/v2/funds/fidc.py">portfolio</a>(\*\*<a href="src/brapi/types/v2/funds/fidc_portfolio_params.py">params</a>) -> <a href="./src/brapi/types/v2/funds/fidc_portfolio_response.py">FidcPortfolioResponse</a></code>
- <code title="get /api/v2/funds/fidc/reports">client.v2.funds.fidc.<a href="./src/brapi/resources/v2/funds/fidc.py">reports</a>(\*\*<a href="src/brapi/types/v2/funds/fidc_reports_params.py">params</a>) -> <a href="./src/brapi/types/v2/funds/fidc_reports_response.py">FidcReportsResponse</a></code>

### Fip

Types:

```python
from brapi.types.v2.funds import FipReportsResponse
```

Methods:

- <code title="get /api/v2/funds/fip/reports">client.v2.funds.fip.<a href="./src/brapi/resources/v2/funds/fip.py">reports</a>(\*\*<a href="src/brapi/types/v2/funds/fip_reports_params.py">params</a>) -> <a href="./src/brapi/types/v2/funds/fip_reports_response.py">FipReportsResponse</a></code>

## Options

Types:

```python
from brapi.types.v2 import (
    OptionSeries,
    OptionChainResponse,
    OptionExpirationsResponse,
    OptionHistoricalResponse,
    OptionStrikesResponse,
)
```

Methods:

- <code title="get /api/v2/options/chain">client.v2.options.<a href="./src/brapi/resources/v2/options/options.py">chain</a>(\*\*<a href="src/brapi/types/v2/option_chain_params.py">params</a>) -> <a href="./src/brapi/types/v2/option_chain_response.py">OptionChainResponse</a></code>
- <code title="get /api/v2/options/expirations">client.v2.options.<a href="./src/brapi/resources/v2/options/options.py">expirations</a>(\*\*<a href="src/brapi/types/v2/option_expirations_params.py">params</a>) -> <a href="./src/brapi/types/v2/option_expirations_response.py">OptionExpirationsResponse</a></code>
- <code title="get /api/v2/options/historical">client.v2.options.<a href="./src/brapi/resources/v2/options/options.py">historical</a>(\*\*<a href="src/brapi/types/v2/option_historical_params.py">params</a>) -> <a href="./src/brapi/types/v2/option_historical_response.py">OptionHistoricalResponse</a></code>
- <code title="get /api/v2/options/strikes">client.v2.options.<a href="./src/brapi/resources/v2/options/options.py">strikes</a>(\*\*<a href="src/brapi/types/v2/option_strikes_params.py">params</a>) -> <a href="./src/brapi/types/v2/option_strikes_response.py">OptionStrikesResponse</a></code>

### Positions

Types:

```python
from brapi.types.v2.options import PositionRetrieveResponse, PositionHistoryResponse
```

Methods:

- <code title="get /api/v2/options/positions">client.v2.options.positions.<a href="./src/brapi/resources/v2/options/positions.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/options/position_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/options/position_retrieve_response.py">PositionRetrieveResponse</a></code>
- <code title="get /api/v2/options/positions/history">client.v2.options.positions.<a href="./src/brapi/resources/v2/options/positions.py">history</a>(\*\*<a href="src/brapi/types/v2/options/position_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/options/position_history_response.py">PositionHistoryResponse</a></code>

### Analytics

Types:

```python
from brapi.types.v2.options import AnalyticsRetrieveResponse, AnalyticsHistoryResponse
```

Methods:

- <code title="get /api/v2/options/analytics">client.v2.options.analytics.<a href="./src/brapi/resources/v2/options/analytics.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/options/analytics_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/options/analytics_retrieve_response.py">AnalyticsRetrieveResponse</a></code>
- <code title="get /api/v2/options/analytics/history">client.v2.options.analytics.<a href="./src/brapi/resources/v2/options/analytics.py">history</a>(\*\*<a href="src/brapi/types/v2/options/analytics_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/options/analytics_history_response.py">AnalyticsHistoryResponse</a></code>

## Futures

Types:

```python
from brapi.types.v2 import (
    FutureQuote,
    FutureSpecs,
    FutureListResponse,
    FutureHistoricalResponse,
    FutureQuoteResponse,
    FutureSpecsResponse,
    FutureTermStructureResponse,
)
```

Methods:

- <code title="get /api/v2/futures/list">client.v2.futures.<a href="./src/brapi/resources/v2/futures/futures.py">list</a>(\*\*<a href="src/brapi/types/v2/future_list_params.py">params</a>) -> <a href="./src/brapi/types/v2/future_list_response.py">FutureListResponse</a></code>
- <code title="get /api/v2/futures/historical">client.v2.futures.<a href="./src/brapi/resources/v2/futures/futures.py">historical</a>(\*\*<a href="src/brapi/types/v2/future_historical_params.py">params</a>) -> <a href="./src/brapi/types/v2/future_historical_response.py">FutureHistoricalResponse</a></code>
- <code title="get /api/v2/futures/quote">client.v2.futures.<a href="./src/brapi/resources/v2/futures/futures.py">quote</a>(\*\*<a href="src/brapi/types/v2/future_quote_params.py">params</a>) -> <a href="./src/brapi/types/v2/future_quote_response.py">FutureQuoteResponse</a></code>
- <code title="get /api/v2/futures/specs">client.v2.futures.<a href="./src/brapi/resources/v2/futures/futures.py">specs</a>(\*\*<a href="src/brapi/types/v2/future_specs_params.py">params</a>) -> <a href="./src/brapi/types/v2/future_specs_response.py">FutureSpecsResponse</a></code>
- <code title="get /api/v2/futures/term-structure">client.v2.futures.<a href="./src/brapi/resources/v2/futures/futures.py">term_structure</a>(\*\*<a href="src/brapi/types/v2/future_term_structure_params.py">params</a>) -> <a href="./src/brapi/types/v2/future_term_structure_response.py">FutureTermStructureResponse</a></code>

### Options

Types:

```python
from brapi.types.v2.futures import (
    FutureOptionSpecs,
    OptionChainResponse,
    OptionExpirationsResponse,
    OptionHistoricalResponse,
    OptionStrikesResponse,
)
```

Methods:

- <code title="get /api/v2/futures/options/chain">client.v2.futures.options.<a href="./src/brapi/resources/v2/futures/options/options.py">chain</a>(\*\*<a href="src/brapi/types/v2/futures/option_chain_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/option_chain_response.py">OptionChainResponse</a></code>
- <code title="get /api/v2/futures/options/expirations">client.v2.futures.options.<a href="./src/brapi/resources/v2/futures/options/options.py">expirations</a>(\*\*<a href="src/brapi/types/v2/futures/option_expirations_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/option_expirations_response.py">OptionExpirationsResponse</a></code>
- <code title="get /api/v2/futures/options/historical">client.v2.futures.options.<a href="./src/brapi/resources/v2/futures/options/options.py">historical</a>(\*\*<a href="src/brapi/types/v2/futures/option_historical_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/option_historical_response.py">OptionHistoricalResponse</a></code>
- <code title="get /api/v2/futures/options/strikes">client.v2.futures.options.<a href="./src/brapi/resources/v2/futures/options/options.py">strikes</a>(\*\*<a href="src/brapi/types/v2/futures/option_strikes_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/option_strikes_response.py">OptionStrikesResponse</a></code>

#### Positions

Types:

```python
from brapi.types.v2.futures.options import PositionRetrieveResponse, PositionHistoryResponse
```

Methods:

- <code title="get /api/v2/futures/options/positions">client.v2.futures.options.positions.<a href="./src/brapi/resources/v2/futures/options/positions.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/futures/options/position_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/options/position_retrieve_response.py">PositionRetrieveResponse</a></code>
- <code title="get /api/v2/futures/options/positions/history">client.v2.futures.options.positions.<a href="./src/brapi/resources/v2/futures/options/positions.py">history</a>(\*\*<a href="src/brapi/types/v2/futures/options/position_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/options/position_history_response.py">PositionHistoryResponse</a></code>

#### Analytics

Types:

```python
from brapi.types.v2.futures.options import AnalyticsRetrieveResponse, AnalyticsHistoryResponse
```

Methods:

- <code title="get /api/v2/futures/options/analytics">client.v2.futures.options.analytics.<a href="./src/brapi/resources/v2/futures/options/analytics.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/futures/options/analytics_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/options/analytics_retrieve_response.py">AnalyticsRetrieveResponse</a></code>
- <code title="get /api/v2/futures/options/analytics/history">client.v2.futures.options.analytics.<a href="./src/brapi/resources/v2/futures/options/analytics.py">history</a>(\*\*<a href="src/brapi/types/v2/futures/options/analytics_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/futures/options/analytics_history_response.py">AnalyticsHistoryResponse</a></code>

## Macro

Types:

```python
from brapi.types.v2 import (
    MacroSeriesAliasWarning,
    MacroSeriesError,
    MacroSeriesObservation,
    MacroSeriesPublic,
    MacroRetrieveResponse,
    MacroLatestResponse,
    MacroListAvailableResponse,
)
```

Methods:

- <code title="get /api/v2/macro">client.v2.macro.<a href="./src/brapi/resources/v2/macro.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/macro_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/macro_retrieve_response.py">MacroRetrieveResponse</a></code>
- <code title="get /api/v2/macro/latest">client.v2.macro.<a href="./src/brapi/resources/v2/macro.py">latest</a>(\*\*<a href="src/brapi/types/v2/macro_latest_params.py">params</a>) -> <a href="./src/brapi/types/v2/macro_latest_response.py">MacroLatestResponse</a></code>
- <code title="get /api/v2/macro/available">client.v2.macro.<a href="./src/brapi/resources/v2/macro.py">list_available</a>(\*\*<a href="src/brapi/types/v2/macro_list_available_params.py">params</a>) -> <a href="./src/brapi/types/v2/macro_list_available_response.py">MacroListAvailableResponse</a></code>

## Treasury

Types:

```python
from brapi.types.v2 import TreasuryListItem, TreasuryListResponse
```

Methods:

- <code title="get /api/v2/treasury/list">client.v2.treasury.<a href="./src/brapi/resources/v2/treasury/treasury.py">list</a>(\*\*<a href="src/brapi/types/v2/treasury_list_params.py">params</a>) -> <a href="./src/brapi/types/v2/treasury_list_response.py">TreasuryListResponse</a></code>

### Indicators

Types:

```python
from brapi.types.v2.treasury import IndicatorRetrieveResponse, IndicatorHistoryResponse
```

Methods:

- <code title="get /api/v2/treasury/indicators">client.v2.treasury.indicators.<a href="./src/brapi/resources/v2/treasury/indicators.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/treasury/indicator_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/treasury/indicator_retrieve_response.py">IndicatorRetrieveResponse</a></code>
- <code title="get /api/v2/treasury/indicators/history">client.v2.treasury.indicators.<a href="./src/brapi/resources/v2/treasury/indicators.py">history</a>(\*\*<a href="src/brapi/types/v2/treasury/indicator_history_params.py">params</a>) -> <a href="./src/brapi/types/v2/treasury/indicator_history_response.py">IndicatorHistoryResponse</a></code>

## User

Types:

```python
from brapi.types.v2 import UserUsageResponse
```

Methods:

- <code title="get /api/v2/user/usage">client.v2.user.<a href="./src/brapi/resources/v2/user.py">usage</a>(\*\*<a href="src/brapi/types/v2/user_usage_params.py">params</a>) -> <a href="./src/brapi/types/v2/user_usage_response.py">UserUsageResponse</a></code>
