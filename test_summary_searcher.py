from summary_searcher import split_summary, get_word_indices


def test_split_summary():
    assert split_summary('a.b.c') == ['a', 'b', 'c']


def test_get_word_indices():
    assert get_word_indices(['the', 'thin', 'the']) == {'the': [0, 2],
                                                        'thin': [1]}
