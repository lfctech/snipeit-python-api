class SnipeITException(Exception):
    """Base exception for all library-specific errors."""
    pass


class SnipeITTimeoutError(SnipeITException):
    """Raised when a request to the Snipe-IT API times out."""
    pass


class SnipeITApiError(SnipeITException):
    """
    Base exception for all errors returned by the Snipe-IT API.

    Attributes:
        message (str): The error message returned by the API.
        response (requests.Response): The full response object.
        status_code (int): The HTTP status code of the response.
    """
    def __init__(self, message, response=None):
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
    """Raised for 422 Unprocessable Entity errors (validation errors)."""
    pass


class SnipeITClientError(SnipeITApiError):
    """Raised for other 4xx client-side errors."""
    pass


class SnipeITServerError(SnipeITApiError):
    """Raised for 5xx server-side errors."""
    pass

