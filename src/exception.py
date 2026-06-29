import sys
import traceback


def error_message_detail(error: Exception) -> str:
    """
    Create detailed error message with file name, line number, and traceback.
    """
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
    line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
    return (
        f"Error in script: [{file_name}] "
        f"at line: [{line_number}] "
        f"message: [{str(error)}]\n"
        f"Traceback:\n{traceback.format_exc()}"
    )


class CustomException(Exception):
    """
    Custom exception class for detailed error reporting.
    """
    def __init__(self, error: Exception):
        self.error_message = error_message_detail(error)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message