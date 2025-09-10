class SnipeITException(Exception):
    """Base exception for all library-specific errors.

    Usage:
        try:
            ...
        except SnipeITException as e:
            # Inspect e for details
            raise
    """
    pass


class SnipeITTimeoutError(SnipeITException):
    """Raised when a request to the Snipe-IT API times out."""
    pass


class SnipeITApiError(SnipeITException):
    """
    Base exception for all errors returned by the Snipe-IT API.

    Attributes:
        response: The full requests.Response (may be None).
        status_code: The HTTP status code if available.
    """
    def __init__(self, message: str, response=None):
        super().__init__(message)
        self.response = response
        self.status_code = response.status_code if response is not None else None


class SnipeITAuthenticationError(SnipeITApiError):
    """Raised for 401 Unauthorized errors."""
    pass


class SnipeITNotFoundError(SnipeITApiError):
    """Raised for 404 Not Found errors."""
    pass


class SnipeITValidationError(SnipeITApiError):
    """Raised for 422 Unprocessable Entity errors (validation errors).

    Attributes:
        errors: Parsed validation errors dict from the API response, if available.
    """
    def __init__(self, message: str, response=None):
        super().__init__(message, response=response)
        self.errors = None
        # Attempt to parse detailed errors from JSON body
        try:
            if response is not None:
                body = response.json()
                self.errors = body.get("errors")
        except Exception:
            self.errors = None


class SnipeITClientError(SnipeITApiError):
    """Raised for other 4xx client-side errors."""
    pass


class SnipeITServerError(SnipeITApiError):
    """Raised for 5xx server-side errors."""
    pass

