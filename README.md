***Readme Under Construction***

# Exclusive Whitening
## Live Website
The live website can be viewed [here](https://ci-pp5.herokuapp.com/).

## Introduction
Exclusive Whitening is a fictional e-commerce fashion retailer based in Ireland. Founded in November 2022, Exclusive Whitening specializes in providing at-home teeth whitening solutions.

That this website is for educational purposes only and the credit card payment functionality is not set up to accept real payments. If testing interactively, feel free to use card details below. Further information can be viewed via Stripe documentation test page.

4242424242424242 (Visa)
Expiration date = Any future date (Example: 12/24)
CVN = any 3 digits (Example: 132)
Postcode = any 5 digits (Example: 12345)

## Showcase
![Screenshot 2022-12-06 at 14 34 35](https://user-images.githubusercontent.com/98256205/205940341-ff00f739-e8ed-4397-8e71-89a525e7bd70.png)

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux-user-experience)
- [Architecture](#architecture)
- [Design](#design)
- [Features](#features)
- [Web Marketing](#web-marketing)
- [Social Media](#social-media)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## UX - User Experience
### User Stories

You can view the kanban board [here](https://github.com/users/martin-mcinerney/projects/4/views/1) and the issues page [here.](https://github.com/martin-mcinerney/CI-PP5/issues)

### Admin 
- As an admin want a panel to create a blog post.
- As an admin want a panel to edit a blog post.
- As an admin want a panel to delete a blog post.
- As an admin I can log in so that I can access superuser privileges.
- As an admin I want a product upload form so that I can upload products on the site.
- As an admin I want a product edit form so that I can edit products on the site.
- As an admin I want a product delete so that I can delete products on the site.

### User
- As a user I can create an account so that I can save and secure my details.
- As a user I can log in so that I can access my account.
- As a user I can log out so that I can secure my account.
- As a user I can view products so that I can choose one to buy.
- As a user I can view product details so that I can learn more about an item.
- As a user I have a filter feature so that I can filter the products.
- As a user I have a search feature so that I can search the database of products.
- As a user I can leave a review on the product so that I can give feedback.
- As a user I have a review edit button so that I can ammend my mistakes.
- As a user I have a review delete button so that I can delete a review.
- As a user I want a shopping bag so that I can add prodcts to it.
- As a user I want an edit bag button so that I can edit quantity in my shopping bag.
- As a user I was a button so that I can delete an item from my bag.
- As a user I want a total so that I can see the total cost of my shopping bag.
- As a user I want a checkout so that I can checkout securely.
- As a user I want a blog page so that I can view blog posts.
- As a user I want a contact page so that I can send a message to the admin.
- As a user I want a navigation bar so that I can nav the website.
- As a user I want an FAQ's page so that I can find out more info.
- As a user I have access to a privacy policy so that I can know my rights.
- As a user I can view a social media page so that I can share the site.
- As a user I have a landing page so that I can land at the site homepage.
- As a user I have messages so that I can receive feedback on my actions.
- As a user I can avail of a responsive design so that I can view the app on mobile or desktop devices.

### Overall Goals
* Create an e-commerce cloud-hosted Full-Stack web application to sell dental products online.
* Allow superusers access to full CRUD (create, read, update and delete) functionality on reviews / articles and products respectively.
* To provide users with a targeted product selection and smooth customer experience when shopping with Exclusive Whitnening.

### Strategy
* Exclusive Whitnening is focused on selling B2C products to end users. Habits of the consumers have changed recently and many more consumers than ever before have turned to home whitening versus in office whitening procedures. This is where Exclusive Whitnening aims to benefit consumers by offering large discounts on the whitening paraphernalia.

### Site User / Target Audience / Demographic
* Target market is aimed at anyone old enough to use the products.
* People who may have stained teeth. eg Smokers, Coffee Drinkers
* People who are interested in dental articles.

### Site Goals
* The site's main purpose is immediately clear
* Simple navigation that allows the user to find information and resources intuitively
* User authentication
* CRUD functionality for superuser(s)

## Architecture
### Database Schema
![Screenshot 2022-12-10 at 08 54 29](https://user-images.githubusercontent.com/98256205/206842117-bbc77406-6da6-42c0-abb5-1d7cb377b06d.png)


## Design
### Wireframes
### Mobile Nav
![Screenshot 2022-12-10 at 10 23 21](https://user-images.githubusercontent.com/98256205/206850201-875cbf80-bbca-4dc2-b958-6806b730127a.png)

### Homepage
![Screenshot 2022-12-10 at 09 13 54](https://user-images.githubusercontent.com/98256205/206850250-45bd165e-c759-4905-9212-41279aed2a3a.png)

### Products
![Screenshot 2022-12-10 at 09 20 32](https://user-images.githubusercontent.com/98256205/206850268-a39c1ca5-de20-424b-bc0a-d47db92a9ee4.png)

### Product Detail
![Screenshot 2022-12-10 at 09 28 32](https://user-images.githubusercontent.com/98256205/206850281-4f6c0d1b-e564-4dc2-8c54-c7361d8aa03a.png)

### Blog
![Screenshot 2022-12-10 at 09 30 29](https://user-images.githubusercontent.com/98256205/206850301-3e10d07d-52f5-4bb8-9e27-12619c8a5e29.png)

### Blog Detail
![Screenshot 2022-12-10 at 09 31 25](https://user-images.githubusercontent.com/98256205/206850320-7b55c610-e04f-4338-9843-4a4e0a12af34.png)

### Contact
![Screenshot 2022-12-10 at 09 41 54](https://user-images.githubusercontent.com/98256205/206850342-ca54fed6-6cf8-42c7-bfa1-866554ef5478.png)

## Navigation
### Entity Relationship Diagram
![Screenshot 2022-12-10 at 11 10 41](https://user-images.githubusercontent.com/98256205/206852111-947e1048-e394-4f02-8b58-d0a4f0001135.png)

## Colour Pallete
![Screenshot 2022-12-10 at 11 29 51](https://user-images.githubusercontent.com/98256205/206852795-8a2f332c-ef21-4043-9d06-005a7b4609fa.png)

## Typography
The site uses "Montserrat" and "Lato" from Google Fonts.

## Features
### Existing Features

