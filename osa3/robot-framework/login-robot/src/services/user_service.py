from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required2")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        #raise UserInputError(f"(username='{username}', password='{password}')", type(username), len(username))

        if not username or not password:
            raise UserInputError("Username and password are required")

        # username: vähintään 3 merkkiä, vain a-z
        if len(username) < 3 or not username.isalpha() or not username.islower():
            raise UserInputError("Invalid username")
    
        # username ei saa olla jo käytössä
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already taken")
    
        # password: vähintään 8 merkkiä
        if len(password) < 8:
            raise UserInputError("Invalid password")
    
        # password ei saa olla pelkkiä kirjaimia
        if password.isalpha():
            raise UserInputError("Invalid password")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
