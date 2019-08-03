[![Build Status](https://travis-ci.org/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce.svg?branch=master)](https://travis-ci.org/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce)

# Project 4 - Ecommerce (full stack web application)
This project is built for [Code Institute](https://codeinstitute.net/) as a part of _Full Stack Software Development Diploma course_. Project was build with using semantic HTML5, CSS3, JavaScript along with Python framework Django 2.2.

Live version deployed on Heroku [here](https://django-ecommerce-milestone.herokuapp.com/).

## UX
This is aiming at people who are looking for buying a kick scooter, eScooter or scooter for kid.

### User Stories

* As a user I want sing up so that I have own account
* As a user I want to login so that I can see my profile page
* As a user I want to logout 
* As a user I want to see my main page as first so that I can easily select which scooter I want
* As a user I want to see shopping cart on every page
* As a user I want to see sammery of my cart so that I can easily see what I am going to buy
* As a user I want to see sammery of my cart so that I can easily remove itmes
* As a user I want to see sammery of my cart so that I can easily amended amount of itmes
* As a user I want to see sammery of my cart so that I can easily see how much it costs
* As a user I want to see checkout so that I can proceed with payment
* As a user I want to see in checkout page a sammery of shopping cart so that I see what I am going to 
* As a user I want to search field so that I can look up a scooter
* As a user I want to see if the scooter is in stock
* As a user I want to use a mobile phone for buying a scooter

### Wireframes:  
The following wireframes were created in order to provide a starting point for the website skeleton:

* [mobile device](wireframes/E-commerce-mobile)
* [desktop device](wireframes/E-commerce-desktop)


## Technologies Used
I used following technologies for this particular project:
* HTML5
* CSS3
   * [Bootstrap](https://getbootstrap.com/)
   * [Font Awesome](https://fontawesome.com/)
* [Python](https://www.python.org/)
   * [Django 2.2](https://docs.djangoproject.com/en/2.2/releases/2.2/)
* Javascript ([jQuery](https://jquery.com/))
* [Stripe](https://stripe.com/)
* [AWS S3](https://aws.amazon.com/s3/)
* [SQLite](https://www.sqlite.org/index.html)
* [Postgresql](https://www.postgresql.org/)
* [Heroku](https://heroku.com/)
* [Adobe Xd](https://www.adobe.com/cz/products/xd.html)
* [VS Studio Code](https://visualstudio.microsoft.com/cs/?rr=https%3A%2F%2Fwww.google.ie%2F)
* [GIMP](https://www.gimp.org/)

# Features
In accordance to the project brief, I have successfully implemented all of the required features.

## Register Account 👤 ➕
   * Anybody can register for free and create their own unique account. This is built using Django's authentication   and authorization to validate profile data. Passwords are hashed for security purposes!

## Change Password 🔐
   * Users can update their passwords from their profile page. They will receive an email with instructions on how    to reset the password.

## Searching scooters
   * Users can easily use search input to find what they are looking for.

## View a particular scooter detail
   * Users can click on a praticular scooter to see details about the choosen scooter.


# Testing 
A thorough mix of automated and manual testing have gone into building the project. In addition to tests, I have validated all files against online validation sites, and checked compatibilities across various modern browsers and devices.

## HTML
* [W3C HTML Validator](https://validator.w3.org/)
   * All 25 .html files have been checked
   * Other validation issues are related to Django Templating not being recognized by W3C:
      * **Warning:** Consider adding a `lang` attribute to the `html` start tag to declare the language of this document
      * **Error:** bad value `{% foo %}`
      * **Error:** Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`
      * **Error:** Element `head` is missing a required instance of child element `title`

## CSS
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   * The W3C Jugsaw validator did not found any errors. Only 3 **warnings**
      * `-webkit-background-size` is an unknown vendor extension
      * `-moz-background-size` is an unknown vendor extension
      * `-o-background-size` is an unknown vendor extension
   

## Contributing
This repository is a part of project for Code Institute of a Full Stack Software Development course. Therefore, I will most likely not accept pull requests.