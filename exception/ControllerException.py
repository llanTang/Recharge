class ControllerException(BaseException):
    def __init__(self,errorCode,message):
        self.errorCode = errorCode
        self.message = message