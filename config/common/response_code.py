# SUCCESS CODE
STATUS_RSP_SUCCESS = 200

# Internal ERROR CODE

# COMMON_ERROR
STATUS_RSP_SIGNATURE_EXPIRED = 401
STATUS_RSP_INTERNAL_ERROR = 4000
STATUS_RSP_UNAUTHORIZED = 4001
STATUS_RSP_INVALID_PARAM = 4002
STATUS_RSP_MISSING_MANDATORY_PARAM = 4003

# USER ERROR

_code_to_message = {
    # SUCCESS
    STATUS_RSP_SUCCESS: 'success',
    STATUS_RSP_SIGNATURE_EXPIRED: 'Signature has expired.',

    # COMMON ERROR
    STATUS_RSP_INTERNAL_ERROR: 'internal server error',
    STATUS_RSP_UNAUTHORIZED: 'unauthorized',
    STATUS_RSP_INVALID_PARAM: 'invalid parameter',
    STATUS_RSP_MISSING_MANDATORY_PARAM: 'missing mandatory parameter',

    # USER ERROR
}


def is_code_success(code):
    if code == 200:
        return True
    return False


def code_to_str(code):
    return str(code)


def code_to_message(code):
    return _code_to_message.get(code)
