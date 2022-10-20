"""
Layer to read json file data which serve to flask rest endpoints
"""
import json
import logging

# Instantiate logger
logger = logging.getLogger(__name__)


class GetCvData:
    """
    Read and handle all data from a json file which is store on disk
    """

    def __init__(self, cv=None):
        self.cv = cv

    def open_and_read(self):
        """
        Open and a json file
        :return: json with all data
        """

        try:
            with open(self.cv) as file:
                # load json first
                data = json.load(file)
            return data
        except (IOError, Exception) as ex:
            logger.error(f'Unable to open json file, reason: {ex}')
            raise ex

    def get_education(self):
        """
        Get education data
        :return: education key value
        """

        try:
            # Initialize variable first
            education = []
            read_data = self.open_and_read()
            # Iterate to get value
            for item in read_data:
                education = item["education"]
            return education
        except KeyError as ex:
            logger.error(f'Unable to find information, reason: {ex}')

    def get_candidate_name(self):
        """
        Get candidate name from json, for multiple candidates
        :return: candidate name
        """
        try:
            # Initialize variable first
            candidate_name = ""
            read_data = self.open_and_read()
            # Iterate to get value
            for item in read_data:
                candidate_name = item["name"]
            return candidate_name
        except KeyError as ex:
            logger.error(f'Unable to find information, reason: {ex}')

    def get_experience(self):
        """
        Get candidate experience
        :return: experience key value
        """
        try:
            # Initialize variable first
            experience = {}
            read_data = self.open_and_read()
            # Iterate to get value
            for item in read_data:
                experience = item["experience"]
            return experience
        except KeyError as ex:
            logger.error(f'Unable to find information, reason: {ex}')


