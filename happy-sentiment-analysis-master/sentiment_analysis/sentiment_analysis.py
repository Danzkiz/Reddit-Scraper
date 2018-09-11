# External dependencies
import logging
import os.path
import sys
import time

# Internal dependencies
from FileParser import FileParser
from SentimentScoreProvider import SentimentScoreProvider 
from TranslateProvider import TranslateProvider 

# Constants
COLUMN_TO_ANALYZE = "labels"
DELAY_SECONDS_BETWEEN_REQUEST_LIMIT = 100
FILE_PATH_CSV = "/usr/src/csv/"
FILE_PATH_RESULTS = "/usr/src/results/"
MAX_NUMBER_OF_REQUESTS = 1000
TRANSLATION_TARGET_LANGUAGE = 'en'

# Logging
logging.basicConfig(level=logging.INFO)

def get_file_name(command_line_arguments):
    result = command_line_arguments[1]
    return result

def get_file_path(base_path, file_name):
    result = os.path.join(base_path, file_name)
    return result

def has_valid_command_line_arguments(command_line_arguments):
    if len(command_line_arguments) >= 1:
        if os.path.isfile(FILE_PATH_CSV + "/" + command_line_arguments[1]) is False:
            logging.error("Could not find file: %s", command_line_arguments[1])
            return False
    else:
        logging.error("Wrong syntax. Usage: python sentiment_analysis.py <filename>")
        return False
    return True

def main():
    command_line_arguments = sys.argv

    if has_valid_command_line_arguments(command_line_arguments):
        file_name = get_file_name(command_line_arguments)
        file_path = get_file_path(FILE_PATH_CSV, file_name)

        logging.info("Parsing file...")
        file_parser = FileParser()
        file_content = file_parser.parse(file_path)
        
        sentiment_score_provider = SentimentScoreProvider()
        translate_provider = TranslateProvider()

        logging.info("Getting and appending translations and sentiment score")
        number_of_requests = 0
        number_of_rows = len(file_content)

        for row in file_content:
            if number_of_requests > 0 and number_of_requests % MAX_NUMBER_OF_REQUESTS == 0:
                logging.info('Waiting %s seconds before sending more requests', DELAY_SECONDS_BETWEEN_REQUEST_LIMIT)
                time.sleep(DELAY_SECONDS_BETWEEN_REQUEST_LIMIT)

            text_answer = row[COLUMN_TO_ANALYZE]
            translated_text_answer = ""
            sentiment_score = {
                'magnitude': "",
                'score': ""
            } 

            if text_answer:
                translated_text_answer = translate_provider.translate(TRANSLATION_TARGET_LANGUAGE, text_answer)
                sentiment_score = sentiment_score_provider.analyze(translated_text_answer)
            
            row['sentiment_magnitude'] = sentiment_score['magnitude']
            row['sentiment_score'] = sentiment_score['score']
            row['translated_' + COLUMN_TO_ANALYZE] = translated_text_answer
            logging.info("Analyzing line %s/%s", str(number_of_requests), str(number_of_rows))
            number_of_requests += 1

        logging.info("Writing new csv file to results folder %s...", file_name)
        result_file_path = get_file_path(FILE_PATH_RESULTS, file_name)
        file_parser.write(result_file_path, file_content)
        logging.info("Done")
    else:
        sys.exit(1)

main()
