from summary_searcher import split_summary


def test_split_summary():
    assert split_summary('a.b.c') == ['a', 'b', 'c']
