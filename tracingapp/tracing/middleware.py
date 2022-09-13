import time
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def response_time_log(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = get_response(request)
        
        # Code to be executed for each request/response after
        # the view is called.
        duration = time.time() - start_time
        logger.debug("{}|{}|{}".format(datetime.now(), request.path, duration))

        return response

    return middleware