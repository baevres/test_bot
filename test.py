import pytest
import setting
from setting import *


class TestForExchange:
    params = [('10 USD to EUR', True),
              ('200 Usd to EuR', True),
              ('14 uah to uah', True),
              ('UH', None)]

    @pytest.fixture(scope='class',
                    params=params)
    def params_test(self, request):
        return request.param

    def test_positive(self, params_test):
        (input_data, expected) = params_test
        input_data = input_data.split(' ')
        result = Exchange(input_data)
        print(f'input: {input_data}, expected: {expected}, result: {result.check_for_exchange()}')
        assert result.check_for_exchange() == expected


class TestForHistory:
    params = [(['USD/EUR', 'for', '2', 'days'], ['USD', 'EUR'], True),
              (['uah/EuR', 'for', '30', 'days'], ['Uah', 'EuR'], True),
              (['USD/UAH', 'for', '0', 'days'], ['USD', 'UAH'], None),
              (['USD', 'for', '7', 'days'], ['USD', ''], None),
              (['USD/EUR', 'for', '7', 'days'], ['', ''], None),
              (['eur/Cad', 'for', '31', 'days'], ['eur', 'Cad'], None)]

    @pytest.fixture(scope='class',
                    params=params)
    def params_test(self, request):
        return request.param

    def test_positive(self, params_test):
        (input_data1, input_data2, expected) = params_test
        result = History(input_data1, input_data2)
        print(f'input: {input_data1}, expected: {expected}, result: {result.check_for_history()}')
        assert result.check_for_history() == expected
