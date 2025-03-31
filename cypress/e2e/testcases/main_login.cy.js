import MainLoginPage from '../../pages/main_login_page';

describe('Main Login Tests', () => {
  const loginPage = new MainLoginPage();

  beforeEach(() => {
    loginPage.visit();
  });

  it('test_login_successful_C01', () => {
    loginPage.login('standard_user', 'secret_sauce');
    cy.url().should('include', '/inventory');
  });

  it('test_login_wrong_password_C02', () => {
    loginPage.login('standard_user', 'wrong_password');
    loginPage.getErrorMessage().should('contain', 'Username and password do not match');
  });

  it('test_login_wrong_username_C03', () => {
    loginPage.login('wrong_username', 'secret_sauce');
    loginPage.getErrorMessage().should('contain', 'Username and password do not match');
  });
});
