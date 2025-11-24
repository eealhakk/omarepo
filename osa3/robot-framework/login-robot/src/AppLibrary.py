from stub_io import StubIO
from repositories.user_repository import UserRepository
from services.user_service import UserService
from app import App

from services.user_service import UserInputError
from repositories import UserRepository



class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)

        self._app = App(
            self._user_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs and value != "Empty":
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_user(self, username, password):
        self._user_service.create_user(username, password)

