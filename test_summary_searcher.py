from summary_searcher import split_summary, get_word_indices, get_inverted_index


def test_split_summary():
    assert split_summary('a.b.c') == ['a', 'b', 'c']


def test_get_word_indices():
    assert get_word_indices(['the', 'thin', 'the']) == {'the': [0, 2],
                                                        'thin': [1]}


def test_get_inverted_index():
    fun_input = {'first': {'the': [0, 2],
                           'thin': [1]},
                 'second': {'the': [0, 2],
                            'dime': [1]}}
    fun_output = {'the': {'first': [0, 2],
                          'second': [0, 2]},
                  'thin': {'first': [1]},
                  'dime': {'second': [1]
                  }}
    assert get_inverted_index(fun_input) == fun_output
