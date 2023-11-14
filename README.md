# Introduction

Contents

- Introduction

Portfolio Project 4 - Waves. This project is a Full-Stack website using the Django framework to build. Waves is a health and fitness website with sea and wellness theme where users can view stunning landscapes and join the community of like-minded people. Users can view posts, comments and the gallery, while registered users can upload posts, create comments and like posts/comments.
   
## CONTENTS

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
  - [Logo and Favicon](#logo-and-favicon)
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

## Typography

The main font used is Quicksand, but Tahoma was used for the main logo appears and the call to action buttons.

## Logo and Favicon

The logo was created using an online logo creator - [Brandcrowd](https://www.brandcrowd.com/)

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

Here is a diagram showing the possible flow through the site. There are 2 sections shown here. On the left it shows the Admin and the right shows a site user.

![Site Flow Diagram]()

## Database Plan

The database plan is fairly simple, but it shows the information that is stored within the database, the type of data and if it is logged as a Primary or Foreign key where applicable.

![Database plan]()

# Features

## Registration

The user can create an account

![Create an Account](documentation/images/create_account.png)

View Blog Posts on Blog Page

![View Blog Posts on Blog Page](documentation/images/home.png)

Browse by Gallery images

![Browse by Gallery Images](documentation/images/browse_by_category.png)

Comment on Blog Posts.

*Also shown here is the trashcan which allows users to delete their own comments should they wish.*

![Comment on Blog Posts](documentation/images/commenting.png)

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





#### Home Page:


| TEST | EXPECTED OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
|:---:|:---:|:---:|
|:---:|:---:|:---:|
|:---:|:---:|:---:|




(*) See Bugs below

## Bugs

One of my users reported that they were unable to sign up when including an email address (although the inclusion of an email address is not required), but myself and others were unable to replicate this issue so the bug was marked as closed.

At different points throughout this project, I encountered various bugs involving the styling. These usually appeared after adding a new section or template page. These were all fixed using Bootstrap classes or custom CSS to override any issues caused by Bootstrap itself.

Towards the end of completion, I had an issue with the database, where I had made a change to the Post Model, but hadn't migrated the changes after undoing the changes in the code relating to that change. This required me to reset the database, which was done with help from Rebecca via the Code Institute's Tutor Support. The changes related to the Category Model and the choices available when creating an account.

To enable me to reset the database, I first had to comment out the code (related to "choices" in the model) to stop the code being run and causing an error. Once this was done, the database was reset, seemingly without issue.

Then I had a problem with the "Create a Post" page. When adding a new blog post via the browser, the images were not being sent to cloudinary for cloud storage, and the ElephantSQL cloud database was also not recieving any data. This was a very simple fix as I needed to add ```enctype="multipart/form-data"``` into the form element.

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

