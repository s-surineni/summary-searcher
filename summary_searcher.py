import json
import logging
import os
import re

logger = logging.getLogger(__name__)


def split_summary(summary):
    return re.split(r'[ \W]+', summary)


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

    except FileNotFoundError:
        logger.error('Make sure youve included file in the folder: {}'
                     .format(os.path.dirname(os.path.realpath(__file__))    
))



prepare_inverted_index()
