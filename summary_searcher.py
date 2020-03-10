from collections import defaultdict
import json
import logging
import os
import re

logging.basicConfig(format='%(filename)s - %(lineno)d - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def split_summary(summary):
    # TODO: Find out a way to remove empty string at last
    return re.split(r'[ \W]+', summary)


def get_word_indices(summary_words):
    word_indices = defaultdict(list)
    for idx, a_word in enumerate(summary_words):
        word_indices[a_word].append(idx)
    return word_indices


def prepare_inverted_index():
    try:
        with open('data.json') as summaries_file:
            title_terms = {}

            summaries = json.load(summaries_file)

            for a_summary in summaries['summaries']:
                summary_text = a_summary['summary']
                # This regex splits the summary on space and
                # punctuation like . , ? etc.,
                summary_text_split = split_summary(summary_text)
                title_terms[a_summary['id']] = summary_text_split

            logger.info('Done splitting summaries into words')
            for a_title_id, summary_words in title_terms.items():
                logger.info('Getting word indices for book {}'.format(a_title_id))
                title_terms[a_title_id] = get_word_indices(summary_words)

    except FileNotFoundError:
        logger.error('Make sure you\'ve included file in the folder: {}'
                     .format(os.path.dirname(os.path.realpath(__file__))    
))


prepare_inverted_index()
