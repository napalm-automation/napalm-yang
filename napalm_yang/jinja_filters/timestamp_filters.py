from datetime import datetime, tzinfo, timedelta
import dateutil.parser
from napalm_yang.jinja_filters.helpers import check_empty

class UTC(tzinfo):
        def utcoffset(self, dt):
            return timedelta(0)
        def tzname(self, dt):
            return "UTC"
        def dst(self, dt):
            return timedelta(0)

EPOCH = datetime.utcfromtimestamp(0).replace(tzinfo=UTC())

def filters():
    return {
        "iso8601_to_unix": iso8601_to_unix,
    }

# Converts an ios8601 formated string into a unix timestamp
@check_empty()
def iso8601_to_unix(string):
    return (dateutil.parser.parse(string) - EPOCH).total_seconds()