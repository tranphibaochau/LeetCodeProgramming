import pytest
from count_and_say import count_and_say


def test_count_and_say():
    test_set = {1: "1",
                2: "11",
                3: "21",
                4: "1211",
                5: "111221",
                6: "312211",
                7: "13112221",
                8: "1113213211",
                9: "31131211131221",
                10: "13211311123113112211"}
    for i in test_set.keys():
        assert count_and_say(i) == test_set[i]
