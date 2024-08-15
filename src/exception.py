import sys  #any exception that is being controlled sys lib will have its info
import logging
from src.logger import logging  # or import logger

def error_message_details(error, error_detail:sys): #error detail contains the detail about error
    _,_,exc_tb = error_detail.exc_info()  #exc_info gives info about error details and we are not intrested in first two thing it return the third thing if where the error has occured, on which line
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

''' simple use
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
'''