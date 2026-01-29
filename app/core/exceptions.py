
class CustomBusinessException(Exception):
    """ Custom base exceptions for all exceptions """
    def __init__(self, message:str,*,code:str,status_code:int=400,details:dict | None = None):
        self.message=message
        self.status_code = status_code
        self.details=details or {}
        self.code = code
        super().__init__(message)


class UserAlreadyExistsException(CustomBusinessException):
    """Exception raised when trying to create a user that already exists."""
    
    def __init__(self,field:str,value:str):
        super().__init__(
            f"User with {field} '{value}' already exists",
            code= "USER ALREADY EXISTS",
            status_code = 409,
            details={"field": field, "value": value}
        )


class UserNotFoundError(CustomBusinessException):
    def __init__(self, field:str, value:str):
        message = f"Email not exist in db field {field}: value {value}"
        status_code=404
        details = {"field": field, "value": value}
        code="USER NOT FOUND"
        super().__init__(message, code=code, status_code=status_code, details=details)


class PasswordNotValid(CustomBusinessException):
    def __init__(self):
        super().__init__(
            "Password not matched with existing",
            code="PASSWORD NOT MATCH",
            status_code=401,
            details={"msg":"password not matched"}
        )

