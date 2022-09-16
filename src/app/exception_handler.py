import sys
import inspect
from app.log import Log
from rest_framework.response import Response

log = Log()


def unpredicted_exception_handler(log_type):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                _, value, traceback = sys.exc_info()
                log('\nTYPE: %s \nFILE: %s \nFUNC: %s \nLINE: %s \nERRR: %s \nINPT: %s' % (log_type, inspect.getfile(
                    func), func.__name__, str(traceback.tb_next.tb_lineno), str(value), str(args) + str(kwargs)))
                return Response("Internal Error", 500)
        return inner

    return decorator
