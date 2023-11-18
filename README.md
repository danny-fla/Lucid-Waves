## Introduction

Portfolio Project 4 - Waves. This project is a Full-Stack website using the Django framework to build. Waves is a health and fitness website with sea and wellness theme where users can view stunning landscapes and join the community of like-minded people. Users can view posts, comments and the gallery, while registered users can upload posts, create comments and like posts/comments.

![Desktop Homepage Wireframe](static/images/responsive.png)
   
## Contents

- [Introduction](#introduction)
  - [CONTENTS](#contents)
  - [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Visitor Goals](#new-visitor-goals)
    - [Existing Visitor Goals](#existing-visitor-goals)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Favicon](#favicon)
  - [Wireframes](#wireframes)
  - [Flow Diagram](#flow-diagram)
  - [Database Plan](#database-plan)
- [Features](#features)
  - [Registration](#registration)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User](#user)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
    - [HTML \& CSS](#html--css)
  - [Python Testing](#python-testing)
  - [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Creating a Fork or Copying](#creating-a-fork-or-copying)
    - [Clone](#clone)
    - [Repository deployment via Heroku](#repository-deployment-via-heroku)
    - [Deployment of the app](#deployment-of-the-app)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___

## Site Objectives

Design and create a blog site to demonstrate an increasing understanding of the libraries and frameworks available to developers.

My three main objectives were:

- ### Develop an Engaging and Responsive User Interface

    The objective was to craft a visually appealing and user-friendly interface. Leveraging the power of Django and Bootstrap, the aim was to ensure readability and ease of navigation for all users.

- ### Implement Robust Backend Functionality

  Utilizing the capabilities of the backend framework, the project aimed to provide users with a seamless experience. Users, whether authenticated through all-auth or alternative methods, could explore posts, comments, and a gallery of images. Additionally, they were empowered to create, edit, and delete their own posts and gallery images.

- ### Utilize External Cloud Database for Data Storage

  To ensure efficient data management, ElephantSQL was employed as the external cloud database, specifically handling the PostgreSQL database for the project. This decision was made to enhance scalability and data accessibility.


By achieving these objectives, the project aimed to showcase an adept understanding of various libraries and frameworks available to developers, delivering a comprehensive and dynamic blog platform.

___

# User Experience/UX

## Target Audience

- Users that are interested in surf, sea and overall wellbeing.

## User Stories

### New Visitor Goals

- Gain a clear understanding of the website's purpose and content.
- Navigate the site effortlessly to explore its features and offerings.
- Create an account to actively engage with the content, other users, and the site owner.

### Existing Visitor Goals

- Log in and out of their account seamlessly.
- Read insightful blog posts, comments and explore the site's gallery.
- Express their views by liking, creating posts, and adding insightful comments to blog posts. Additionally, users can actively participate in the creation, editing, and liking of gallery images.

___

# Design Choices

## Colour Scheme

The chosen color scheme for this project mirrors the vibrant hues of the site's banner, capturing the essence of a sunset atop a rolling wave. The palette exudes warmth to encapsulate the sun's radiance, coupled with subtle tones of darkness to signify the shadow cast, and touches of white to convey the transparent and fluid nature of water.

![Colour Palette](static/images/colour-palette.png)

## Typography

The main font used is Quicksand, but Tahoma was used for the main logo appears and the call to action buttons.

![Font](static/images/font.png)


## Wireframes

- Mobile Homepage Wireframe

![Mobile Homepage Wireframe]()

- Mobile Post Detail Wireframe

![Mobile Post Detail Wireframe]()

- Desktop Homepage Wireframe

![Desktop Homepage Wireframe]()

- Desktop Post Detail Wireframe

![Desktop Post Detail Wireframe]()

## Flow Diagram

### Admin Flowchart

![Admin Flow Diagram](static/images/admin-flowchart.png)

### User Flowchart

![User Flow Diagram](static/images/user-flowchart.png)

## Database Plan

![Database plan](static/images/db-diagram.png)

# Features

### Home Page

![Home Page](./assets/readme/features/tasty_blog_home-page.jpg)

* The hero image welcomes the user with a short message advertising what the website is about. These
are 3 carousel images with a button. When the button is pressed, it brings the user down to the highlighted recipes.<br>

### Home Page - Highlight Posts

![Home Page - Highlight Posts](./assets/readme/features/tasty_blog_home_page_highilights-.jpg)

* In the highlighted posts, users can see a selection of 6 recipes. These recipes are
chosen by the site admin by clicking the featured box in the post database.<br>

### About Page

![About Page](./assets/readme/features/tasty_blog_about_page.jpg)

* The About Page gives, users information about the Tasty Blog website. It introduces the users to the
website. It also details the main purpose and the goal of the blog.<br>

### Blog Page

![Blog Page](./assets/readme/features/tasty_blog_page.jpg)

* On the Blog Page, users have access to the full recipes posts available on the website.
The user can choose to see the recipe detail by clicking on the recipe card.<br>

### Post Detail Page - Top

![Post Detail Page - Top](./assets/readme/features/tasty_blog_post_detail_1_page.jpg)

* At the top of the Post Details Page, users can see the post's main
image and they can also have access to information about the post. The
post information includes category, recipe name, rating stars,
time to prepare, author name and image, posted date and the
option to like/unlike the post. It will also show how many likes and
comments the post has received.<br>

### Post Detail Page - Steps

![Post Detail Page - Steps](./assets/readme/features/tasty_blog_post_detail_2_page.jpg)

* In this page section, users can read the ingredients and follow the steps to complete the recipe.<br>

### Post Detail Page - Comments

![Post Detail Page - Comments](./assets/readme/features/tasty_blog_post_detail_comments_page.jpg)

* At the bottom of this page, users can read the comments posted by other users. If the user is logged in or is a 
superuser they have access to the buttons for deleting or updating comments.

### Edit Comments Page

![Edit Comments Page](./assets/readme/features/tasty_blog_edit_comments_page.jpg)

* On this page, users are allowed to comment, delete and edit their own post comments. The website superuser can 
  delete or update any comments on the blog without having to access the admin panel.

### Contact Page

![Contact Page](./assets/readme/features/tasty_blog_contact_page.jpg)<br><br>

* The Contact Page allows users to have access to the Tasty blog
contact details. Users can also send an email to info@tastyblog by
using the contact form available on this page.

### Categories Page

![Categories Page ](./assets/readme/features/tasty_blog_categories_page.jpg)<br><br>

* On the Categories Page, users can see the categories available in the blog and filter the posts by category.

### Categories Results

![Categories Results Page](./assets/readme/features/tasty_blog_categories_results_page.jpg)

* On the Categories Results Page, users can access the post filtered by the chosen category.
  
### Books Page

![Books Page](./assets/readme/features/tasty_blog_books_page.jpg)

* On this page, registered users can see favourite books posted by other users. If they had already published 
  a post they are allowed to edit or delete their own posts

### Add/Edit Books Page

![Add/Edit Book Page](./assets/readme/features/tasty_blog_add_book_page.jpg)

On this page, registered users can fill out the form to add or edit a post with their favourite cookbooks.

### Search Box

![Search Box](./assets/readme/features/tasty_blog_search_page.jpg)

* In this box, the users can search by inputting a keyword in the search tool. This allows the user to try and find 
  the recipe they are looking for.

### Search Results Page

![Search Results Page](./assets/readme/features/tasty_blog_search_results_page.jpg)

* On the Search Results Page, users can see the recipes found by their search.  When their recipe is located, the user can go to the 
  Post Details Page by clicking on the card result.

### Search Results - Input Empty

![Search Results - Input Empty](./assets/readme/features/tasty_blog_search_results_empty_page.jpg)

* On the Search Results Page - Input Empty, users will see this message if their search returns with an empty input.

### Search Results - No Results Found

![Search Results - No Results Found](./assets/readme/features/tasty_blog_search_results_null_page.jpg)

* On the Search Results Page - No Results Found, users will see this message if there is nothing found for the search.

### Signup Page

![Signup Page](./assets/readme/features/tasty_blog_signup_page.jpg)

* On the Signup Page, a new user can sign up for the Tasty Blog website by filling out and then submitting the form.

### Login Page

![Login Page](./assets/readme/features/tasty_blog_login_page.jpg)

* On the Login Page, users can log in to the website by inputting the username and password and have access 
  to website services for a user registered.

### Logout Page

![Logout Page](./assets/readme/features/tasty_blog_logout_page.jpg)

* On the Logout Page, users can confirm that they wish to exit the website.

### User Profile Page

![User Profile Page](./assets/readme/features/tasty_blog_user_profile_page.jpg)

* On the Profile Page, users have access to their own information and can update their user name, email and profile image.

### Navbar

![Navbar](./assets/readme/features/tasty_blog_navbar.jpg)

* The navigation bar is present at the top of every page and houses all links to the various other pages.
* The options to Register or Log in will change to the option to log out once a user has logged in.
* Once a user has signed in, more options such as profile page and user image will be available in the navbar.
* A search icon is nested in the navbar and once clicked it will open the search box.
* The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

![Navbar](./assets/readme/features/tasty_blog_navbar_dropdown_menu.jpg)
* In the navbar users can access the categories list by clicking on the dropdown menu.

### Footer

![Footer](./assets/readme/features/tasty_blog_footer.jpg)
* On the website footer, users can see basic information about the blog such as contact, social media, 
  copyright, and a quote about food recipes.

## Messages and Interaction With Users

* Some interactive messages were added to the project to make the navigation on the website easier and to improve the
user's experience.

### Sign up

![Sign up](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_signup.jpg)

* When users sign up to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>

### Login

![Login](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_login.jpg)

* When users sign in to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>

### Logout

![Logout](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_logout.jpg)

* When users log out of the website they will see a message at the top of the page saying "You have signed out".<br>
  
### Profile Update

![Profile Update](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_profile_update.jpg)

* When users update their profile they will see a message at the top of the page saying that their account has been updated.<br>

### Like Post

![Like Post](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_like_post.jpg)
* *When users are logged in to the website they can like a post and they will see a message at the top of the page 
  saying "You have liked this post".<br>

### Unlike Post

![Unlike Post](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_unlike_post.jpg)

* When users are logged in to the website they can unlike a post that has been liked by the user and they will see a message 
  at the top of the page saying "You have unliked this post".<br>

### Comment Post

![Comment Post](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_sent_1.jpg)

* When users are logged in to the website they can comment on a post and after they submit the comment they will see a 
  message at the top of the page saying "Your comment was sent successfully and is awaiting approval".<br>

### Comment Post - 2

![Comment Post - 2](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_sent_2.jpg)

* After a user submits a comment, they will see a message over the input comment saying "Thanks (username). Your 
  comment is awaiting approval! <br>

### Delete/Edit Comment

![Delete Comment](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_delete_1.jpg)

* When users are logged in to the website and they have previously posted a comment or if the user is a superuser they will see the 
Delete and Edit buttons at the bottom of comments.<br>

### Delete Comment - 1

![Delete Comment - 2](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_delete_2.jpg)

* If they wish to delete their comment, they can press the button Delete and a Bootstrap box model will pop up with the message 
  "Are you sure you want to delete your comment?".<br>

### Delete Comment - 2

![Delete Comment - 3](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_delete_3.jpg)

* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your comment was deleted successfully".<br>

### Edit Comment

![Edit Comment](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_edit.jpg)

* After pressing the Update, users will see a message on the top of the page, "The comment was successfully updated".<br>

### Email Sent - Success

![Email Sent - Success](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_email_sent_2.jpg)

* After users submit the form to info@tastyblog successfully, they will see the message, "Thanks for your email! 
  We will contact you as soon as possible".<br>

### Email Sent - Failed

![Email Sent - Failed](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_email_sent.jpg)

* If the email was not submitted successfully, users will see the message, "Sorry, something went wrong! 
  Try to submit the email again".<br>

### Add Book

![Add Book](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_add_book.jpg)  

* When users are logged in to the website they can publish a post with a favourite cookbook and after they submit the 
post they will see a message at the top of the page saying "Your post was sent successfully and is awaiting approval".<br>

### Edit Book

![Edit Book](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_book_edit.jpg)  
* When users are logged in to the website they can edit their own previously published posts and they will see the message 
  "The post was successfully updated" after pressing the Submit button.<br>

### Delete Book 1 

![Delete Book 1](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_book_delete_2.jpg)
When users are logged in to the website and they wish to delete their posts, they can press the button Delete and a 
Bootstrap box model will pop up with the message "Are you sure you want to delete your post?".<br>  

### Delete Book 2

![Delete Book 2](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_book_delete.jpg)  

* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your post was deleted successfully".<br>

### Empty Search

![Empty Search](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_profile_empty_search.jpg)

* Any user can search for a keyword using the input search and if the search is done with an empty input they will see a
  message saying, "You forgot to search a recipe. Please try searching again.".<br>

### No Search Found

![No Search Found](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_profile_no_search_found.jpg)

* And if there are no results matching or similar to the keyword, the user will see the following message, "We are sorry. 
  There are no searches for (keyword) on the website. Try the search again".<br>

## Admin Panel/Superuser
![No Search Found](./assets/readme/extras/tasty_blog_superuser.jpg)

* On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and
delete the following ones:
1. Posts
2. Comments
3. Author
4. Categories
5. Profiles
6. Books
   
*As admin/superuser I can also approve comments, approve posts and change the status and give other permissions to the users.<br>

## Future Features

-

## Features Not Included

- 

___

# Technologies Used

Here are the technologies used to build this project:

- [GitPod](https://gitpod.io/) To build and create this project
- [Github](https://github.com) To host and store the data for the site.
- [GitPod](https://www.gitpod.io) the IDE where the site was built.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Used as cloud storage for images uploaded as part of the blog posts
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

# Agile

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub

- [Project Board]()

# Testing

As each section or Function/Model was built during this project, I was testing for functionality and styling issues that may have arisen (see table below), which were corrected or fixed before continuing. I also had friends test the site by signing up, adding and deleting comments using various devices on varying platforms (IOS, Android, Mobile, Tablet etc) and reporting back any issues they encountered with functionality or styling.

## Manual Testing

*For any Fails, there is a more detailed description below the table*

## ADMIN

#### Login and Authentication:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Log in with valid admin credentials.|Successful login, and the admin dashboard is displayed.|Pass|
| Log in with invalid credentials.|Appropriate error message displayed.|Pass|



#### Post Management:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create a new blog post.|Post is successfully created and listed in the admin interface.|Pass|
|Edit an existing blog post.|Changes are saved, and the post is updated.|Pass|
| Delete a blog post.|Post is removed from the system.|Pass|
|Like a post|The like count is incremented, and the user's like is recorded.|Pass|
|Unlike a post.|The like count is decremented, and the user's like is removed.|Pass|



#### Comment Management:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|View a list of comments.| All comments are displayed in the admin interface.|Pass|
| Approve a pending comment.|Comment status changes to approved.|Pass|
|Delete a comment.|Comment is removed from the system.|Pass|
|Like a comment|The like count is incremented, and the user's like is recorded.|Pass|
|Unlike a comment.|The like count is decremented, and the user's like is removed.|Pass|



####  Gallery Management:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Upload a new image to the gallery.| Image is successfully uploaded and listed in the admin interface.|Pass|
| Edit details of an existing gallery image.|Changes are saved, and the image details are updated.|Pass|
|Delete a gallery image.|Image is removed from the system.|Pass|
|Like a gallery image.|The like count is incremented, and the user's like is recorded.|Pass|
|Unlike a gallery image.|The like count is decremented, and the user's like is removed.|Pass|



#### User Management:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|View a list of users.|All users are displayed in the admin interface.|Pass|
|Edit user details.| Changes are saved, and user details are updated.|Pass|
|Suspend a user account.|User account is suspended.|Pass|



#### Settings


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Modify general site settings.|Changes are saved, and settings are updated.|Pass|
|Change the admin password.|Password is successfully updated.|Pass|




#### Security


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Access admin URLs without authentication.|Access should be denied, and the user redirected to the login page.|Pass|
| Log out from the admin interface.|User is logged out, and the login page is displayed.|Pass|




#### Overall Assessment

- The admin site should handle CRUD operations effectively for posts, comments, the gallery and users.
- Authentication and authorization mechanisms should be robust to ensure secure access to admin functionalities.
- All actions should result in the expected outcomes as defined in the "Expected Output" sections.


## User


#### Home Page:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Access the home page|Home page is displayed with a welcoming message and featured content|Pass|
|Navigate to the gallery|Gallery page is accessible from the home page|Pass|
|Navigate to the blog|Blog page is accessible from the home page|Pass|




#### Gallery:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|View gallery images|Gallery displays a grid of images with captions|Pass|
|Hover over an image|Image overlay displays image owner, edit & delete options, caption and like button & counter|Pass|
|Like an image|Like count increments, and the user's like is recorded|Pass|
|Unlike an image|Like count decrements, and the user's like is removed|Pass|




#### Blog:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|View blog posts|Blog page displays a list of posts with titles and excerpts|Pass|
|Click on a post|Full post is displayed with details, author, and comments|Pass|
|Like a post|Like count increments, and the user's like is recorded|Pass|
|Unlike a post|Like count decrements, and the user's like is removed|Pass|
|Add a comment|Comment is added to the post|Pass|




#### User Account:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Register a new account|Account is created successfully, and the user is logged in|FAIL|
|Log in with existing credentials|Successful login, and the user is redirected to the home page|FAIL|
|Log out from the account|User is logged out, and the login page is displayed|FAIL|




#### Navigation:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Navigate using the menu bar|Menu items lead to the respective pages (Home, Gallery, Blog, Login, Register)|Pass|
|Use pagination on blog page|Clicking on page numbers displays the corresponding posts|Pass|
|Use pagination on gallery page|Clicking on page numbers displays the corresponding iamges|FAIL|




#### Responsiveness:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Access the site from various devices (desktop, tablet, mobile)|Site content adapts appropriately to different screen sizes|FAIL|





#### Overall Site Functionality:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Check for broken links|All links navigate to the correct pages|Pass|
|Test social media sharing buttons|Buttons allow users to share content on social media|FAIL|
|Test overall site performance|Pages load within a reasonable time frame|Pass|




#### Security:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|Access user-specific pages without authentication|Access should be denied, and the user redirected to the login page|Pass|
|Log out from the user interface|User is logged out, and the login page is displayed|Pass|




## Bugs

### Problem Description:

I encountered a major issue during a recent database update for my web project "Lucid Waves," developed using Django. The primary key, acting as a unique ID for database entries, started displaying a date and time instead of a regular number. This unexpected behavior disrupted database updates and led to malfunctions on the website.

### Troubleshooting Steps:

1. Review of Model Definitions:
    - Carefully examined the model definitions, especially focusing on the 'GalleryImage' model where the issue occurred.
    - Ensured that the primary key field was correctly defined as an AutoField for the 'id'.

2. Examination of Migration Files:
    - Checked the migration files to identify any custom operations or changes that might affect the primary key field.
    - Ensured that the migration files were in sync with the model definitions.

### Further Interaction with Tutor:

1. Database Reset Suggestion:
    - Based on the observed error and actions taken, the tutor suggested there might be corrupted or conflicting data in the database.
    - Together, we considered the option of a database reset, involving the deletion of all posts, comments, etc.

2. Migrations Deletion Guidance:
    - Tutor guided on deleting all migration files, excluding the __init__.py file, to address potential migration-related issues.

3. Database Reset Execution:
    - Implemented the tutor's guidance, resetting the database using ElephantSQL, and subsequently running makemigrations and migrate commands.

### Collaborative Resolution:

The issue was effectively resolved through a collaborative effort, with both parties actively contributing to the troubleshooting process. The collaborative approach ensured a shared understanding of the problem and the implementation of solutions, fostering a sense of joint accomplishment.

### Key Takeaways:

1. Shared Troubleshooting:
    - The collaborative effort underscored the importance of jointly reviewing and addressing issues for a more comprehensive resolution.

2. Effective Communication:
    - Clear and effective communication between both parties facilitated a better understanding of the problem and the actions taken.

3. Skill Development:
    - The collaborative resolution process served as a valuable learning experience, contributing to the development of debugging and troubleshooting skills.

### Conclusion:

The collaborative resolution of the primary key issue reflects the effectiveness of teamwork in problem-solving. This experience not only led to a successful outcome but also contributed to a shared learning journey in maintaining and debugging Django projects.

## Lighthouse

The performance scores appear to be low, and I believe this is due to the images uploaded for each blog post being hosted on a third-party cloud-based platform.

Mobile

![Lighthouse Mobile Score](documentation/images/lighthouse_mobile.png)

Desktop

![Lighthouse Desktop Score](documentation/images/lighthouse_desktop.png)

## Validation Testing

### HTML & CSS

HTML & CSS testing was completed using [W3 Validator](https://validator.w3.org/)

When validating the code, I had the error shown below. this was fixed by removing the button and using Bootstrap styles to display the link as a button instead

![HTML Validation - Descendant Error](documentation/testing_documentation/validation/base.html_button_descendant.png)

Fixed:

![HTML Validation Complete- base.html](documentation/testing_documentation/validation/index.html_validation_complete.png)

## Python Testing

Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

