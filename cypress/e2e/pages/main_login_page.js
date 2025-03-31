import MainLoginLocators from '../locators/main_login_locators';

class MainLoginPage {
  visit() {
    cy.visit('/');
  }

  login(username, password) {
    cy.get(MainLoginLocators.USER_NAME_FIELD).type(username);
    cy.get(MainLoginLocators.PASSWORD_FIELD).type(password);
    cy.get(MainLoginLocators.LOGIN_BUTTON).click();
  }

  getErrorMessage() {
    return cy.get(MainLoginLocators.LOGIN_ERROR);
  }
}

export default MainLoginPage;
