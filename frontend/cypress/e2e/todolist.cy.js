describe('Add new todo item', () => {
  let uid // user id
  let name // name of the user (firstName + ' ' + lastName)
  let email // email of the user
  before(function(){
    // create a fabricated user from a fixture
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
          email = user.email
        })
      })
  })

  beforeEach(function(){
    cy.visit('http://localhost:3000/')

     // detect a div which contains "Email Address", find the input and type (in a declarative way)
    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type(email)
    // alternative, imperative way of detecting that input field
    //cy.get('.inputwrapper #email')
    //    .type(email)

    // submit the form on this page
    cy.get('form')
      .submit()
    
    cy.contains('div', 'Title')
      .find('input[type=text]')
      .type('Motivation')
    
    cy.contains('div', 'YouTube URL')
      .find('input[type=text]')
      .type('dQw4w9WgXcQ')
    
    cy.get('form')
      .submit()
  })

  it('add button is disabled', () => {
    cy.get(':nth-child(1) > a ')
      .click()

    cy.get('.inline-form > [type="submit"]')
      .should('be.disabled')
  })

  it('add button is enabled', () => {
    cy.get(':nth-child(2) > a ')
      .click()

    cy.get('.inline-form > [type="text"]')
      .type('Play on repeat')
    
    cy.get('.inline-form > [type="submit"]')
      .should('be.enabled')
  })

  it('todo item is added to list', () => {
    cy.get(':nth-child(3) > a ')
    .click()

    cy.get('.inline-form > [type="text"]')
      .type('Play on repeat')
    
    cy.get('.inline-form > [type="submit"]')
      .click()
  
    cy.get('.todo-list > :nth-child(2) > .editable')
      .should('contain.text', 'Play on repeat')
  })

  it('todo item gets deactivated', () => {
    cy.get(':nth-child(4) > a ')
    .click()

    cy.get('.inline-form > [type="text"]')
      .type('Play on repeat')
    
    cy.get('.inline-form > [type="submit"]')
      .click()
  
    cy.get('.todo-list > :nth-child(2) > .checker')
      .click()
    cy.get('.todo-list > :nth-child(2) > .checker')
      .should('have.class', 'checker checked')
  })

  it('todo item gets activated', () => {
    cy.get(':nth-child(5) > a ')
    .click()

    cy.get('.inline-form > [type="text"]')
      .type('Play on repeat')
    
    cy.get('.inline-form > [type="submit"]')
      .click()
  
    cy.get('.todo-list > :nth-child(2) > .checker')
      .click()
      .click()
    
    cy.get('.todo-list > :nth-child(2) > .checker')
      .should('have.class', 'checker unchecked')
  })

  it('todo item gets deleated', () => {
    cy.get(':nth-child(6) > a ')
    .click()

    cy.get('.inline-form > [type="text"]')
      .type('Play on repeat')
    
    cy.get('.inline-form > [type="submit"]')
      .click()
  
    cy.get(':nth-child(2) > .remover')
      .click()

    cy.get('.todo-list')
      .its('length')
      .should('be.lte', 2)
  })

  after(function () {
    // clean up by deleting the user from the database
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  
  })
})