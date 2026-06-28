import sys

def error_message_detail(err, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{err}]"
    return error_message

class CustomException(Exception):
    def __init__(self, err_message, error_detail: sys):
        super().__init__(err_message)
        self.err_message = error_message_detail(err_message, error_detail=error_detail)

    def __str__(self):
        return self.err_message