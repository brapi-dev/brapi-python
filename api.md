# Quote

Types:

```python
from brapi.types import (
    BalanceSheetEntry,
    CashflowEntry,
    DefaultKeyStatisticsEntry,
    FinancialDataEntry,
    IncomeStatementEntry,
    ValueAddedEntry,
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
from brapi.types.v2 import CurrencyRetrieveResponse, CurrencyListAvailableResponse
```

Methods:

- <code title="get /api/v2/currency">client.v2.currency.<a href="./src/brapi/resources/v2/currency.py">retrieve</a>(\*\*<a href="src/brapi/types/v2/currency_retrieve_params.py">params</a>) -> <a href="./src/brapi/types/v2/currency_retrieve_response.py">CurrencyRetrieveResponse</a></code>
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
