describe('Main Login Tests', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('test_login_successful_C01', () => {
    cy.login('standard_user', 'secret_sauce');
    cy.url().should('include', '/inventory');
  });

  it('test_login_wrong_password_C02', () => {
    cy.login('standard_user', 'wrong_password');
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match');
  });

  it('test_login_wrong_username_C03', () => {
    cy.login('wrong_username', 'secret_sauce');
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match');
  });
});
