from pages.API_page import UserAPIPage, PetAPIPage
from configs.api_parsing import *
import allure



class TestAPI:
    api_user = UserAPIPage()
    api_pet = PetAPIPage()

    @allure.feature('API user module')
    @allure.story('Create user')
    def test_create_user(self):
        with allure.step('Get status code after user creation'):
            result = self.api_user.create_user()
            with allure.step('Check if status code == 200'):
                assert result == 200, f"Error, response: {result}"

    @allure.feature('API user module')
    @allure.story('User log in positive')
    def test_log_in_user_positive(self):
        with allure.step('Get status code after user log in'):
            result = self.api_user.login()
            with allure.step('Check if status code is 200'):
                assert result == 200, f"Error, response: {result}"

    @allure.feature('API user module')
    @allure.story('User log in negative')
    def test_log_in_user_negative(self, status):
        with allure.step('Get status code after user log in'):
            result = self.api_user.login()
            with allure.step('Check if status code is not wrong'):
                assert result != status, f"Error, response: {result}"

    @allure.feature('API user module')
    @allure.story('Get info about user')
    def test_get_user_info(self):
        with allure.step('Get info of created user'):
            result = self.api_user.get_user_info()
            with allure.step('Check if info is the same as filled in info'):
                assert result == user_info, f"Error: result is {result}"

    @allure.feature('API user module')
    @allure.story('User log out')
    def test_log_out(self):
        with allure.step('Get status code after user log out'):
            result = self.api_user.logout()
            with allure.step('Check if status code == 200'):
                assert result == 200, f"Error, response: {result}"

    @allure.feature('API user module')
    @allure.story('Delete user positive')
    def test_delete_user_positive(self):
        with allure.step('Get status code after user is deleted'):
            result = self.api_user.delete_user()
            with allure.step('Check if status code is 200'):
                assert result == 200, f"Error, response: {result}"

    @allure.feature('API user module')
    @allure.story('Delete user negative')
    def test_delete_user_negative(self, status):
        with allure.step('Get status code after user is deleted'):
            result = self.api_user.delete_user()
            with allure.step('Check if status code is not wrong'):
                assert result != status, f"Error, response: {result}"

    @allure.feature('API pet module')
    @allure.story('Pet creation')
    def test_create_pet(self):
        with allure.step('Get status code after pet creation'):
            result = self.api_pet.create_pet()
            with allure.step('Check if status code == 200'):
                assert result == 200, f"Error, response: {result}"

    @allure.feature('API pet module')
    @allure.story('Check info about pet')
    def test_check_pet_info(self):
        with allure.step('Get info of created pet'):
            result = self.api_pet.check_pet_info()
            with allure.step('Check if info is the same as filled in info'):
                assert result == pet_info, f"Error: result is {result}"

    @allure.feature('API pet module')
    @allure.story('Check pets new name (update)')
    def test_update_pet_name(self):
        with allure.step('Update name of created pet'):
            result = self.api_pet.update_pet_name()
            with allure.step('Check if name is updated'):
                assert result == new_pet_name, f"Error: result is {result}"
