

# Created @ 4-Apr-2025 Tuesday
# Author: Salman Ahmad

'''
Contains log class for the Media Manager App
'''

from datetime import datetime as dt
from dotenv import load_dotenv
import os

# loading enviourmnetal variables into our code
load_dotenv(dotenv_path='media_manager/.env')

# Log class
class Logging:
    '''
    Logs various parameters of Media Manager like while inserting movies or reading emails from Excel file etc.
    '''

    # data members
    logger_name = None
    today = None
    date = None
    time = None
    day = None
    year = None
    month = None
    __fd = None
    __log_repo = os.getenv('LOG_PATH')
    __log_file_name = None

    # Constructor
    def __init__(self, logger_name: str = None) -> None:
        # assigning values to data members
        self.logger_name = logger_name
        self.today = dt.today()
        self.date = self.today.date()
        self.time = self.today.time().strftime('%H:%M:%S')
        self.day = self.today.day
        self.year = self.today.year
        self.month = self.today.month

        # creating log file name
        self.__log_file_name = f"{self.logger_name}_{self.year}_{self.month}_{self.day}_{self.today.strftime('%H_%M_%S')}.txt"
        self.__fd = open(file='media_manager/logs/' + self.__log_file_name, mode='w+')

    # __str__
    def __str__(self):
        message = f'[LOGGER] {self.logger_name}\n'
        message = message + f'[LOGGER] [YEAR] -> {self.year}, [MONTH] -> {self.month}, [DAY] -> {self.day}, [DATE] -> {self.date}, [TIME] {self.time}'
        return message
    

    # format_now
    def format_now(self):
        return f'{self.year}-{self.month}-{self.day} {self.today.strftime('%H:%M:%S')}'
    

    # log_starting_details_to_file
    def log_starting_details_to_file(self) -> None:
        # logging details to file
        message = f"Logger initialized with the name -> {self.logger_name}.\n"
        message = message + f'AUTHOR: {self.logger_name}\n'
        message = message + f'Created at: {self.format_now()},\t(Year, Month, Date)\n'
        self.__fd.write(message)

    # write
    def write(self, write_base: str = None):
        self.__fd.write(write_base)