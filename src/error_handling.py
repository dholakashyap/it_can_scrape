```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidURLError(Error):
    """Exception raised for errors in the input URL.

    Attributes:
        url -- input url which caused the error
        message -- explanation of the error
    """

    def __init__(self, url, message="Invalid URL provided. Please check the URL and try again."):
        self.url = url
        self.message = message
        super().__init__(self.message)

class InvalidFieldError(Error):
    """Exception raised for errors in the input fields.

    Attributes:
        fields -- input fields which caused the error
        message -- explanation of the error
    """

    def __init__(self, fields, message="Invalid field(s) provided. Please check the fields and try again."):
        self.fields = fields
        self.message = message
        super().__init__(self.message)

class PaginationError(Error):
    """Exception raised for errors in the pagination parameter.

    Attributes:
        pagination -- input pagination which caused the error
        message -- explanation of the error
    """

    def __init__(self, pagination, message="Invalid pagination parameter provided. Please check the pagination parameter and try again."):
        self.pagination = pagination
        self.message = message
        super().__init__(self.message)

class AsyncError(Error):
    """Exception raised for errors in the async parameter.

    Attributes:
        async_param -- input async parameter which caused the error
        message -- explanation of the error
    """

    def __init__(self, async_param, message="Invalid async parameter provided. Please check the async parameter and try again."):
        self.async_param = async_param
        self.message = message
        super().__init__(self.message)
```