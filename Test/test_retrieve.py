import pytest
from Data import retrieve_data


def test_get_historical_data():
    # create an instance of retrieve_data
    dt_len = 78
    rd = retrieve_data.RetrieveData()
    # get the historical data
    data = rd.get_historical_data('TSLA', '5minute', 'day', 'regular')
    print(len(data))
    # check if the data is not None
    assert data is not None
    # check if the data is of the correct length
    assert len(data) == dt_len
