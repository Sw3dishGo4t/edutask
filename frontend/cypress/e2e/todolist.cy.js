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
    
  })

  it('add button is disabled', () => {
    
  })

  it('add button is enabled', () => {
    
  })

  it('todo item is added tp list', () => {
    
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