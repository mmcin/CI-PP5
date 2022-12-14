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
### Homepage
Here we can see the nav bar along with the authentication options. User can sign up to mailing lists. Hero section has a CTA leading customers to the products section where they can make a purchase. Nav bar and footer are visible here. They expand as shown below.

![Screenshot 2022-12-10 at 11 49 49](https://user-images.githubusercontent.com/98256205/206857077-cda9b66e-63f0-426d-8e0c-1bd53aea7798.png)
![Screenshot 2022-12-10 at 11 50 12](https://user-images.githubusercontent.com/98256205/206857084-0f510d6e-928c-43ff-98ad-65e292c6f4ef.png)

![ci-pp5 herokuapp com_(Martinas Monitor)](https://user-images.githubusercontent.com/98256205/206853704-e39eb2f8-cde2-40c7-b3a1-27873a1c93e3.png)

### Products
Here the products are listed. Out of stock items are marked as such. Clicking the item image leads to the product detail page.
![ci-pp5 herokuapp com_products_(Martinas Monitor)](https://user-images.githubusercontent.com/98256205/206853757-6500ef9f-2f67-4235-ae29-8877e2eac7c6.png)

### Product Detail
Here there are details on a product. Reviews are displayed if applicable. Super users can edit or delete a product. Logged in users can review a product. If the admin approves the review it will be displayed. I had hoped to add the logic to the program that checked if the user had bought a product in the past but it proved beyond the scope of the timeframe. I have used Javascript to make sure that the buttons don't let you add more items than are in stock. The issue with this is that if you reload the page, you can add them again. Products are not removed from the inventory until sold. I'd like to add some logic to reserve products in future but this was the most appropriate solution at the moment.
![ci-pp5 herokuapp com_products_3_(Martinas Monitor)](https://user-images.githubusercontent.com/98256205/206853770-9f0232e8-ace0-4487-9ae0-7b3b1a609f1c.png)

### Blog
Admin controlled blog page. Posts are added in Django admin panel. Click to open and lead to Blog Detail page.
![ci-pp5 herokuapp com_blog_posts_(Martinas Monitor)](https://user-images.githubusercontent.com/98256205/206853783-b293822a-9bb4-433b-946c-4823caa9ab56.png)

### Blog Detail
Opens the blog post into a fuller view so that the body can be read.
![ci-pp5 herokuapp com_blog_post_ice-can-be-nice_(Martinas Monitor)](https://user-images.githubusercontent.com/98256205/206853791-34204f42-8671-4be3-83e1-77fb73b50de7.png)

### Contact
Contact form that stores messages in the database.
![ci-pp5 herokuapp com_contact_contact_(Martinas Monitor)](https://user-images.githubusercontent.com/98256205/206853809-2a57c941-45e5-4fdd-8b36-4efb41c870ef.png)

### Profile
Users profile info. Their address will auto fill at checkout.
![ci-pp5 herokuapp com_profile_ (2)](https://user-images.githubusercontent.com/98256205/206856035-09d3aff1-e754-467f-955e-84ebf83969fd.png)

### Shopping Bag
Items that have been placed in the bag are displayed and the checkout can be accessed from here. I have added logic so that if the user has more product quantity than is in stock, the product quantity will be reduced to the number left in stock and a message displayed.
![ci-pp5 herokuapp com_bag_](https://user-images.githubusercontent.com/98256205/206856055-97830d4a-75f7-4373-aa4f-c57e08041721.png)

### Checkout
Fill out to buy the products in the bag. Please use the test values to make a payment. 
![ci-pp5 herokuapp com_checkout_ (1)](https://user-images.githubusercontent.com/98256205/206856083-135d4a2d-5fca-4f1f-9039-192342b1f015.png)

### Checkout Success
An order was successfully placed. A confirmation email is sent. This logic is triggered by Stripe webhooks ensuring that the order is created should the user close the page during payment processing. 
![ci-pp5 herokuapp com_checkout_checkout_success_74DC5ECABEFF4FD4875D304CDCD1524C (2)](https://user-images.githubusercontent.com/98256205/206856149-d5203b26-d190-46cf-881e-6c649c04ca78.png)

### Product Management
Admin can add a product.
![ci-pp5 herokuapp com_products_add_](https://user-images.githubusercontent.com/98256205/206856248-5e5ee1b7-46c7-4fe5-8a6d-c3a0eb076878.png)

### Log In
![ci-pp5 herokuapp com_accounts_login_](https://user-images.githubusercontent.com/98256205/206856546-6d886e78-e75c-4929-a9cf-a98819d2946b.png)


### Log Out
![Screenshot 2022-12-10 at 13 00 27](https://user-images.githubusercontent.com/98256205/206856552-1676e225-7624-49c3-917d-b49e2dc68977.png)


### Sign Up
![ci-pp5 herokuapp com_accounts_signup_](https://user-images.githubusercontent.com/98256205/206856531-cd5ff3b9-fbf9-486b-b077-c63291019b3e.png)


### Forgot Password
![ci-pp5 herokuapp com_accounts_password_reset_](https://user-images.githubusercontent.com/98256205/206856529-ea9c1163-7d25-400c-a8c0-1b19c4535ae2.png)

## Web Marketing / Marketing Strategies
### SEO
Google keyword research was used to optimise web pages and content to increase ranking in search engines. Both short-tail & Long-tail keywords are used. The “People also ask” and “Related searches” was also used to identify keywords used.
![Screenshot 2022-12-10 at 13 28 39](https://user-images.githubusercontent.com/98256205/206857619-ef5ae51d-4a56-4ec1-b005-2ab4523d2a00.png)

### Content Marketing
A blog post was created so that the website can create and distribute content material to attract and convert audience into first time customers and repeat customers. The main aim of the blog posts is to build trust and loyalty.

### Social Media Marketing
A Facebook business page was set up with the aim of generating growth organically by building a community and encouraging loyalty amongst our target market. The advantage of this is its free and quick to set up and Facebook has a large audience and demographic. The site can connect with customers directly via the Facebook platform and wider global audience. The main aim of the Facebook page is to build and maintain relationship with target audience. Content created can be spread across different social media platforms.
![www facebook com_profile php_id=100088602249685](https://user-images.githubusercontent.com/98256205/206858801-e9ecb782-4afc-407f-873e-d3f619dcd4bd.png)

### Email Marketing
Mailchimp is used to gain new customers and retain existing. Mailchimp enables the business to run and analyse the success of newsletter marketing campaigns. Users who register to receive the newsletter are automatically added to weekly newsletter. This strategy was chosen because its free to set up with the current level of business and can scale quickly as the business grows therefore increase conversions and generate more revenue for the business. The users who sign up have already visited the website and are more likely to become customers and therefore low cost to generate sales.

### Frameworks, Libraries & Programs Used
* [Amazon S3](https://aws.amazon.com/s3/) service offered by Amazon Web Services that provides object storage through a web service interface.
* [amiresponsive](http://ami.responsivedesign.is/) to see how responsive the site is on different devices.
* [Balsamiq](https://balsamiq.com/) was used to create the Wireframes.
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) v4.6 was used to help build responsive, mobile-first design.
* [Color-hex](https://www.color-hex.com/) once I identified the colors I wanted I used color-hex to generate the palette.
* [Django](https://www.djangoproject.com/) free and open-source, Python-based web framework that follows the model–template–views architectural pattern.
* [Font Awesome](https://fontawesome.com/) was used for icons for aesthetic and UX purposes on the buttons.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
* [Gitpod](https://www.gitpod.io/) An online IDE linked to the GitHub repository used to write my code.
* [Google Chrome Dev tools](https://developer.chrome.com/docs/devtools/) for debugging.
* [Google Fonts](https://fonts.google.com/about) for typography.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) used for audits to measure the quality of web pages.
* [Google Keyword Planner](https://ads.google.com/aw/keywordplanner/home?)
* [Heroku](https://www.heroku.com/) used to deploy this app, a cloud platform as a service supporting several programming languages.
* [Pexels](https://www.pexels.com/) Images for this project were sourced from Pexels.
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/) Free Privacy Policy Generator.
* [Stripe](https://stripe.com/en-ie) Integrated with Stripe to facilitate online payments.
* [SQLite](https://www.sqlite.org/index.html) database used in local development was a SQLLite database.
* [Terms and Conditions Generator](https://www.termsandconditionsgenerator.com/) Free terms and conditions generator.
* [Unsplash](https://unsplash.com/) Images for this project were sourced from Unsplash.
* [WAVE](https://wave.webaim.org/extension/) Browser Extension testing.
* [Wordtracker](https://www.wordtracker.com/)
* [a11y](https://color.a11y.com/) Color Contrast Accessibility Validator.

## Testing
### Lighthouse
My homepage has a few accessibility errors that are due to the nav bar setup. All pages have above 90% scores except for in accessibility where the nav layout having two elements with the same id brings the score down. Also there is an error asking to surround the mobile nav li items in an ul or ol. This is not neccesary so I am ignorning it and have added some tags for screenreaders.
![googlechrome github io_lighthouse_viewer_](https://user-images.githubusercontent.com/98256205/206860255-c6792f58-514d-4e23-99e8-b41b357e8750.png)

### HTML Validation
HTML files that have been validated with W3.
- index.html
- products.html
- product_detail.html
- add_product.html
- edit_product.html
- bag.html
- checkout.html
- checkout_success.html
- contact.html
- profiles.html
- 404.html
- blog.html
- blog_detail.html

### W3C CSS Validator
Checked using W3C CSS Validator ensuring there were no errors or warnings present.

### Python Validation
I used autopep8 to validate all the Python files and checked them with Flake8.

### JSHint
I checked the JS files with JSHint for conformity.

### Color Contrast Accessibility Validator
The site passed the color contrast test on https://color.a11y.com/ 

### Accessibility
The WAVE WebAIM web accessibility evaluation tool was used for browser extension testing to ensure no errors shown

### Manual Testing
### More manual testing scenarios and results
| Feature | Test  | Expected Result | Actual Result |
| -------------| ----- | ----- | :----: |
| XY logo  | Selecting XY logo on homepage |  directs user back to homepage |  Pass |
| Navigation Links  | Selecting navigation links |  directs user to relevant categories & pages |  Pass |
| All categories  | Selecting All for each category |  directs user to show all relevant categories on the same page |  Pass |
| Sort By  | Selecting the filter Sort by for each category |  successfully alters the search By price, name and category options reflects results accordingly on page |  Pass |
| Contact Us | Selecting Contact Us |  directs user to Contact Us page |  Pass |
| Shop Now | Selecting Shop Now |  directs user to full products list page |  Pass |
| Blog | Selecting Blog |  directs user to Blog page |  Pass |
| Blog Detail | Selecting Blog Detail |  directs user to Blog Detail page |  Pass |
| Submitting Review Form | Editing details in review form on Products |  successfully edits message to admin and displays success message |  Pass |
| Submitting Edit Review Form | Submitting  details in review form on Products |  successfully sends message to admin and displays success message |  Pass |
| User Access | Logged in as user |  I can leave a review comment on products |  Pass |
| User Access | Logged in as user and author |  I can edit a review comment on products |  Pass |
| User Access | Logged in as user and author |  I can delete a review comment on products |  Pass |
| Form Validation Required fields | Filling in form on /contact page | requires name, email and body and contact reason selected to send to Django admin  |  Pass |
| Contact form submission | submit contact form | successfully sends data to Django admin as expected  |  Pass |
| Register | Register for an account | selecting Register in my account directs user to /accounts/signup/ page |  Pass |
| Login | Login to an account | selecting Login in my account directs user to /accounts/Login/ page |  Pass |
| Search | Using the search box | Entering a search returns expected result  |  Pass |
| Back to top | Back to top box | Selecting the back to top box on the products pages brings the user back to the top of the page  |  Pass |
| Search no results | No search | Entering a no results search returns error message and shows all products  |  Pass |
| New User | Registering as a new user | Registering as a new user entering form validation works |  Pass |
| Admin | Loggin in as Logging in as superuser / admin | Logging in as superuser / admin directs user to admin access, shows product management page |  Pass |
| Login Message | log-in Success | "successfully signed in as (user name)" message shown to user|  Pass |
| Add Product | Adding a new product | Adding a new product on the product management page successfully adds product |  Pass |
| Add Product | no image is selected | default image is used |  Pass |
| Deleting Product | Deleting selected product | removed product from search |  Pass |
| Deleting Message | Deleting product confirmation | Confirmation message of deletion is shown when successfully deleted |  Pass |
| Deleting Message | Deleting product confirmation | Confirmation message of deletion is shown when successfully deleted |  Pass |
| Defensive Programming | Test for SQL Injection attacks | Users not permitted to access create/update/delete products articles or reviews if they don't have access permission | Pass |
| Logging out | message shown | Logging out as a user / admin prompts "are you sure" message |  Pass |
| Successfully signed out | signed out message shown | "You have signed out" message shows to user when successfully signed out |  Pass |
| Logging out | Logging out and redirect | Logging out as a user / admin directs user to homepage |  Pass |
| Footer | social media links | Clicking on the social media icons in the footer open the link in a new tab |  Pass |
| Footer | Privacy Policy links | Clicking on the Privacy Policy link in the footer diverts user to the /privacy/ page |  Pass |

### Responsiveness Browser Compatibility

|  | Chrome | Firefox | Edge | Safari | Pass/Fail |
| ------------- |-------------| -----|  ---------- |  -----| :----: |
| Expected Appearance   | yes | yes  | yes  | yes | Pass |
| Expected Layout   | yes | yes  | yes  | yes | Pass |

## Bugs / Errors encountered during development
* “can’t open file ‘manage.py’: [Error 2] No such file or directory”. Reason why was there is a character missing character in the command used for starting the project
*  I tried using Whitenoise to host staticfiles for a while after getting scared for my money due to AWS budget notices. I would get Django errors because I was stashing my media files in the static directory. This meant that I had the filing system set up weird and didn't have working file service in production with debug to true. This lead me to miss the error log that was leading me on a wild goose chase when trying to use Stripe webhooks to trigger a confirmation email. (see below)
*  I couldn't get the payment intent succeeded webhook to work. I dragged the http response to the top of the handler fucntion and it was working fine so it was begin sent alright. I couldn't see the error as debug was on false due to the above issue. In the end it was due to missing email template files that I had forgotten to write.
*  Product detail quantity buttons were allowing users to add more than the allowed items in stock. This would be very bad for a business so I implemented some custom JS that would disable the button when the stock level had been reached. 
*  Customers could add 10 items if there were ten in stock but then they could reload the page and add another 10. To protect against this I decided to add some code that would automatically redice the bag quantity of a product to the number left in stock if they had more than was available in their bag. A message was added for this.
*  In order to solve the above bug I had to display the stock quantity of products and add an out of stock message.

## Stripe
* Register for an account at stripe.com
* Go to Developers section once logged in
* Go to API keys section
* Note both the publishable and secret keys
* In your local environment(env.py) and Heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')
os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')
* Back in the Developers section of your stripe account click on Webhooks
* Create a webhook with the url of your website /checkout/wh/, for example:
* Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
* Note the key created for this webhook
* In your local environment(env.py) and Heroku, create environment variable STRIPE_WH_SECRET with the secret values os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')
* Test the webhook and note the success/fail attempts for troubleshooting, see events and logs for further testing.

## Amazon WebServices
* Create an account at aws.amazon.com
* Open the S3 application and create an S3 bucket named "ci-pp5
* Select AWS Region.
* Uncheck the "Block All Public access setting" & acknowledge that the bucket will be public, it will need to be public in order to allow public access to static files.
* In the Properties section, navigate to the "Static Website Hosting" section and click edit
* Under the Properties section, turn on "Static Website Hosting", and set the index.html and the error.html values.
* In the Permissions section, click edit on the CORS configuration and set the below configuration
* Click to edit the bucket policy and generate and set the below configuration:
* Bucket policy
* Go to the Access Control List and set the List objects permission for everyone under the Public Access section.
* Open the IAM application to control access to the bucket and set up a user group called
* Click on Policies, and Create Policy.
* Click on the JSON tab and import a pre-built Amazon policy called AmazonS3FullAccess:
* Set the following settings in the JSON tab:
* Click Review Policy, give it a name and description and click Create Policy.
* To attach the policy to the group, navigate to Groups, then Permissions, and under Add Permissions, select Attach Policy.
* To create a user for the group, click Add User, and create one
* Add the user to the group created, making sure to download the CSV file which contains the user's access credentials.
* Note the following AWS code in Settings.py. An environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage:
* 
## Google Email
* Create an email account at google.com, login, go to accounts settings in your gmail account and then click on Other Google Account Settings
* Go to accounts and import then click on other account settings
* Under signing into Google, turn on 2-step verification and follow the steps to enable
* Once verified click on app passwords, select Other as the app and give the password a name, for example Django
* Click create and a 16 digit password will be generated, copy this 16 digit password
* In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
* In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
* Set and confirm the following values in the settings.py file to successfully send emails
* You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

## Deployment

* This project was developed using a GitPod workspace. The code was committed to Git and pushed to GitHub using the terminal.

* Log in to [Heroku](https://id.heroku.com/login) or create an account
* On the main page click New and Create New App
* Note: new app name must be unique
* Next select your region, I chose Europe.
* Click Create App button
* Click in resources and select Heroku Postgres database
* Click Reveal Config Vars and add new config "SECRET_KEY"
* Click Reveal Config Vars and add new config "DISABLE_COLLECTSTATIC = 1"
* The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
* Next, go to Buildpack section click Add Buildpack select python and Save Changes
* Scroll to the top of the page and choose the Deploy tab
* Select Github as the deployment method
* Confirm you want to connect to GitHub
* Search for the repository name and click the connect button
* Scroll to the bottom of the deploy page and select the preferred deployment type
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github
* As Heroku Student Pack no longer includes free access to the Postgres add-on I had to migrate Postgres databases from Heroku to keep ElephantSQL.
* Navigate to ElephantSQL.com and click “Get a managed database today”
* Select “Try now for FREE” in the TINY TURTLE database plan
* Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account
* In the Create new team form

### Migrating databases
* Create a database
* Log in to ElephantSQL.com to access your dashboard
* Click “Create New Instance”
* Set up your plan
* Select “Select Region” EXAMPLE "EU-West-1 (Ireland)"
* Then click “Review”
* Check your details are correct and then click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name for this project

### Migrating your data
* Navigate to the Postgres Migration Tool repo on github in a new browser tab
* Click the Gitpod button to open a new workspace
* Run the script " python3 reel2reel.py" command in the terminal
* In a different browser tab, go to your app in Heroku and select the Settings tab
* Click the “Reveal Config Vars” button
* Copy the value in the DATABASE_URL Config Var. It will start with postgres://
* Return to Gitpod and paste in the URL you just copied into the terminal where prompted to provide your DATABASE_URL and click enter
* In your original browser tab, get your ElephantSQL database URL. Again, it will start with postgres://
* Return to Gitpod and paste in the URL where prompted
* The data will now be downloaded from Heroku and uploaded to your ElephantSQL database
* To test that your database has been moved successfully, return to ElephantSQL and select BROWSER
* Click the “Table queries” button. If you see any options in the dropdown, your tables have been created
* Select a table name you recognise, and then click “Execute”
* You should see your data displayed relating to the table you selected

### Connecting ElephantSQL database to Heroku
* In the Heroku Dashboard for your project, open the Resources tab
* In the Resources tab, remove the existing Postgres add-on:
* Confirm by typing in the name of your Heroku app when prompted.
* Navigate to the Settings tab
* Reveal your existing Config Vars. The original DATABASE_URL should have been deleted when the add-on was removed.
* Add a new config var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.
* Check the Activity tab to confirm


### Final Deployment 

* Create a runtime.txt `python-3.8.14`
* Create a Procfile 
* When development is complete change the debug setting to: `DEBUG = False` in settings.py
* In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

### Forking This Project

* Open [GitHub](https://github.com/martin-mcinerney/ci-pp5)
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository

### Cloning This Project / Local Deployment

* Clone this project by following the steps:

* Open [GitHub](https://github.com/martin-mcinerney/ci-pp5)
* You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
* Once you click the button the fork will be in your repository
* Open a new terminal
* Change the current working directory to the location that you want the cloned directory
* Type 'git clone' and paste the URL copied in step 3

```git clone https://github.com/martin-mcinerney/ci-pp5```

* Press 'Enter' and the project is cloned to your workspace
* Create an env.py file(do not commit this file to source control) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<br><code>import os</code>
<br><code>os.environ["SECRET_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["STRIPE_PUBLIC_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["STRIPE_SECRET_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["STRIPE_WH_SECRET"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["AWS_ACCESS_KEY_ID"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["AWS_SECRET_ACCESS_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["EMAIL_HOST_USER"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["EMAIL_HOST_PASS"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["USE_AWS"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["DATABASE_URL"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["DEVELOPMENT"] ='True'</code>

* Some values for the environment variables above are described in different sections of this readme
* Install the relevant packages as per the requirements.txt file
* In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
* Ensure debug is set to true in the settings.py file for local development
* Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
* Run "python3 manage.py showmigrations" to check the status of the migrations
* Run "python3 manage.py migrate" to migrate the database
* Run "python3 manage.py createsuperuser" to create a super/admin user
* Run manage.py loaddata db.json to load the product data into the database
* Start the application by running <code>python3 manage.py runserver</code>
* Open the application in a web browser, for example: http://127.0.0.1:8000/

## Credits

* Code Institute - [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/) -  Walkthrough
* Code Institute - [Hello Django](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/121ef050096f4546a1c74327a9113ea6/) -  Walkthrough
* Code Institute - [I think therefore I blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/
) - Django blog project Walkthrough
* Hillbox - My Code Intitute PP4
* Style Django Forms With Bootstrap 
 [YouTube](https://www.youtube.com/watch?v=6-XXvUENY_8)
* More Django Styling  
 [YouTube](https://www.youtube.com/watch?v=uJp4PaDkux0)
* Richard Sherry - I found the answers to many of my questions about the PP5 by reading Richard's readme and code.
* The great Bootstrap and Django docs
* Pexel for the images
 

## Acknowledgements
* To create this website, I relied on material covered in the Full Stack Development course by Code Institute.
* I also sourced information and help from a variety of sources such as Slack Community Channels, Udemy, W3Schools, MDN and YouTube for Online Web Tutorials and resources.
* Martina Terlevic for being a great mentor and helping me to undertstand how to build a more robust application.
* Michael Mc for testing the site.
* Viv for feeding me during my long days and nights stuck at the keyboard.

This project is for educational use only and was created for the Code Institute Module.

Martin McInerney
