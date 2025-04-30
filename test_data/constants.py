import random

class TestData:
    USER_EMAIL = "<enter valid email>@hudl.com" #Please enter a valid email address
    USER_PASSWORD = "<enter valid pwd>" #Please enter a valid password
    INCORRECT_EMAIL = "test" + str(random.randint(1000, 9999)) + "@example.com" #dynamic email address to prevent locking an account after too many login failures
    INCORRECT_PASSWORD = "1234!"
    INVALID_EMAIL_FORMAT = "TEST@"
    INVALID_PASSWORD = "1234!"
    URL = "https://identity.hudl.com/u/login/identifier?state=hKFo2SBxSU1DZWV1RThOTll3RlBzRUMwMGRyN1lkZzVTeE1ncKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIDlJQVBUSWh3QmI5Y3o4NzBDUUpEN1JubzllSHdkWVRXo2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"
    INVALID_EMAIL_ERROR_MESSAGE = "Enter a valid email."
    INVALID_EMAIL_OR_PASSWORD_ERROR_MESSAGE = "Incorrect username or password."
