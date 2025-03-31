import MainLoginPage from '../../pages/main_login_page';
const tools = require('../../../tools.json');

describe('Main Login Tests', () => {
  const loginPage = new MainLoginPage();

  beforeEach(() => {
    loginPage.visit();
  });

  it('test_login_successful_C01', () => {
    loginPage.login(tools.login.username, tools.login.password);
    cy.url().should('include', '/inventory');
  });

  it('test_login_wrong_password_C02', () => {
    loginPage.login(tools.login.username, 'wrong_password');
    loginPage.getErrorMessage().should('contain', 'Username and password do not match');
  });

  it('test_login_wrong_username_C03', () => {
    loginPage.login('wrong_username', tools.login.password);
    loginPage.getErrorMessage().should('contain', 'Username and password do not match');
  });
});
