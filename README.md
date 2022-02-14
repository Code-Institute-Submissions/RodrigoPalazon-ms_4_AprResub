# The ROCKShow Store

## The ROCKShow is a fictional online musical instruments store. The stores purpose is to sell different types of instruments, such as Guitar, Drums, Bass, and Keyboard. The store will allow the owner to make more sales by moving to an online platform. 

#### The live website can be viewed [PUT YOUR LINK here]()

<br>

## Table Of Contents 

- <a href="#ux">UX</a>
  - <a href="#user-stories">User Stories</a>
  - <a href="#strategy">Strategy</a>
  - <a href="#scope">Scope</a>
  - <a href="#structure">Structure</a>
- <a href="#database">Database</a>
- <a href="#wireframes">Wireframes</a>
- <a href="#surface">Surface</a>
- <a href="#crud">CRUD</a>
- <a href="#features">Features</a>
- <a href="#languages">Languages</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

<br>

<span id="ux"></span>

## UX 

<span id="user-stories"></span>

### User Stories 

**As a New User**

* I want to be able to use the site intuitively. 
* I want to be able to search for products.
* I want to be able to view the details of individual products.
* I want to be able to order products by category.
* I want to be able to order products by finer details such as A-Z, price low to high or vice versa. 
* I want to be able to add products to my basket and checkout, without an account.
* I want to be shown messages throughout my journey through the site.
* I want to be able to register an account.

**As a Site Owner/Super User**

* I want to have a payment system implemented.
* I want to be able to edit product details.
* I want to be able to add new products.
* I want to encourage returning users by having an easy to use site.
<!-- * I want to have a contact form where users can send any questions. -->

**As a Returning User/Signed In User**

* I want to be able to edit my delivery address and information.
* I want to have a personalised profile that shows any previous orders.
* I want to be able to log in to a previously registered profile. 
* I want to be able to leave reviews for products.

**Key Benefits Of Having An Account**
* As a registered user, you can leave a review of a product. A non registered user can not.
* As a registered user, you have a profile. Here you can view previous orders and save default delivery information. A non registered user does not have a profile.

<span id="strategy"></span>

### 1.Strategy 

**Project Goals**

* To make a full-stack site based around business logic used to control a centrally-owned database.
* To make a full-stack site that uses HTML, CSS, JavaScript, Python + Django.
* Creating a website that uses a relational database.
* Creating a website that uses Stripe payments.

**Site Owner Goals(Business Goals)**

* Creating a secure, professional and profitable e-commerce website.
* Inspire users to play music and initialize a new hobby.

<span id="scope"></span>

### 2.Scope

* Fits in with my current skill-set of HTML, CSS, JavaScript, Python and Django.

<span id="structure"></span>

### 3.Structure

**As A New User (Not Logged In)**

A new user can visit:
  * The home page
  * Can access the register and login pages 
  * The products page
  * Sign up for newsletter on contact page
  * Specific category pages
  * The basket
  * The checkout
  <!-- * Contact form -->


**As A Registered User (Logged In)** 
A returning user can visit:
  * The home page
  * Can access the log out functionality
  * Profile, to save details and view previous orders.
  * Leave a review function
  * The products page
  * Sign up for newsletter on contact page
  * Specific category pages
  * The basket
  * The checkout
  <!-- * Contact form -->

**As Superuser (Site Owner)**
A superuser can visit:
  * The home page
  * Can access the log out functionality
  * Profile
  * Product management (Add a product)
  * Edit a product
  * Delete a product
  * Send a newsletter to subscribers
  * The products page
  * Specific category pages
  * The basket
  * The checkout
  <!-- * Contact form -->

<span id="database"></span>

### Database 

* During the development phase I used the sqlite3 database.
* For deployment, I used the PostgresSQL database which is provided by Heroku.

### Database Models

<br>
