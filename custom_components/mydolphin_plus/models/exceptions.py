class LoginError(Exception):
    def __init__(self, message: str = "Failed to login"):
        super().__init__(message)
        self.error = message


class TransientLoginError(LoginError):
    """Cognito could not be reached or answered with a server error.

    The stored credentials are not known to be bad, so callers should retry
    later instead of discarding tokens and asking the user to log in again.
    """
