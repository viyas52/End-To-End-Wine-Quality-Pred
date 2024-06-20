import sys
from src import logging

def error_message_datail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f'Error occures in python script name {file_name} line number {exc_tb} error message {str(error)}'
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_datail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message