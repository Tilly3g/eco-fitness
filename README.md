# Eco Fitness

<a href="https://snyk.io/test/github/Tilly3g/eco-fitness?targetFile=requirements.txt"><img src="https://snyk.io/test/github/Tilly3g/eco-fitness/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/Tilly3g/eco-fitness?targetFile=requirements.txt" style="max-width:100%;"></a>


This is a website where a user can go if they want to become healthier both mentally and physically but also want to help the environment at the same time. They can use the calorie calculator in the food diary to track their eating and book in sessions with fitness experts for meal and exercise plans that include eco friendly swaps.

The site is mobile friendly as well as working on larger screen sizes.

## UX

The website is designed for users who are looking to become healthier and also more eco friendly in their day to day lives.

The navigation bar has clearly labled options so it is easy for a user to navigate around the site. They can either search the available bookings or add food to the food diary using the search function. This calculates how much they ahve eaten and how many calories they have remaining of the recommended daily amount.

They can update or remove items in their basket and can remove items in their diary as well. The diary is only available for user who have an account and so encourages people to sign up. all actions also include useful message popups so the site is really clear and easy to understand what you are doing.

User stories:

1. To have a website where I can book sessions with experts who can help me with meal and fitness plans, and eco friendly swaps.

- To acheive their goal, the above user type would only need to open up Eco Fitness, navigate to 'Book Now' and choose a booking type. They can then add their desired number of sessions to their basket. From their a popup will show them what is in the basket and the option to view and pay or an error if there is one. The checkout flow works and takes test payments successfully to confirm bookings.

2. To have the ability to save booking information and previous order history within the site.

- The above user type can do this by logging in or creating an account either before or during the checkout flow - it is clearly labled that they need to login or create account to save billing information during the flow. They can sign up, receive authentication email, authenticate and then sign in successfully. 

3. To be able to add and remove nutritional information to their food diary in order to calculate how much they have eaten and how many calories they would have left of the daily recommended amount.

- The above user would only need to login or create an account in order to achieve the above. When they login they will then see the food diary option in the navigation and also on the homepage. The food diary is described on the homepage and the user is told they need to login or signup in order to use this. They can then add food items with total calories calculated for them and they can remove these items as well.

4. To be able to search for food items using general terms and categories.

- The above user can search the database using any terms within the food name or category. They can also click on a category tag from search results or nutritional information pages to view all foods within that category.

5. To be able to add a certain amount of food to the food diary to track calories accuarately.

- The above user can do this by entering the amount of food in grams that they want to calculate the calories for.

3. To be able to add and remove food items and available bookings as a site admin.

- The above user can do this by logging in to the site and then navigating to either 'Booking management' or 'Nutrition management' to add new booking types or nutritional information for new foods. They can also edit or remove exisiting bookings and foods by navigating to either the nutritional information of the food they want to edit or the 'Manage' option which is visible for admins on the 'Book now' page.

## Existing Features

- Navigation bar - allows user to easily move between pages of the website depending on what they want to do.
- Search bar - allows user to search by food name or category.
- Add booking - allows users to add the chosen booking type to their bag (and choose an amount).
- Add food - allows users to add food (of a chosen amount in grams) to their food diary and calculator.
- Food diary - allows user to calculate how many calories they have eaten and shows remaining of the average daily recommended amount. 
- View nutritional information - allows user to view all available nutritional information for the chosen food type.
- Remove food - allows users to remove food items from the food diary.
- Remove or update booking - allows users to remove or update the amount of any session type in their basket before paying.
- Make secure payment - allows customer to pay for their bookings securely using Stripe

## Features Left to Implement

- In the future I would like to add a page that shows pictures and introductions to each expert available.
- another feature I would like to add would be the ability to save the items in the food diary per day and navigate back to a previous day to view what was eaten.

## Technologies Used

- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    - To allow the use of prebuilt layouts and CSS for styling elements.

- [jQuery](https://jquery.com/)
    - To allow the use of certain pre-written functions.

- [Google Fonts](https://fonts.google.com)
    - To allow the use of a wider range of fonts.

- [Django](https://www.djangoproject.com/)
    - To use the django framwork for the app, including all the features such as creating accounts.

- [AWS](https://aws.amazon.com/console/)
    - To store files.

- Python
    - To render each page template and incorporate the information from the database.

- Javascript
    - For the funcionality of the framwork.

- HTML
    - For the design and background elements.

- CSS
    - To style the HTML.

## testing

1. Navigation Bar: All the buttons on the nav bar are linked to the correct page and they also collapse down when the screen size is made smaller.
2. Search bar: The search bar functions by searching for the search term within either the food name or category and displays all results. The user is notified if no results are found.
3. Add food or booking: All required feilds must be filled in and the character limits must be honoured or an error explaining the problem is shown in.
4. Edit food or booking: All required feilds must be filled in and the character limits must be honoured or an error explaining the problem is shown in. The entry is then successfully updated in the database.
5. Delete food or booking from diary or bag respectively: This feature successfully removes the items from teh bag or diary and updates the totals correctly. 
6. Messages: messages popup for all user actions as expected.
7. Add food or booking to diary or bag respectively: This feature successfully adds the items from the bag or diary and updates the totals and amounts correctly. 
8. Edit quantity of session type in bag: This functions correctly and clicking update will change the subtotal and total correctly as well as the quantity.
9. Delete food or booking from database as admin: This feature successfully removes the items from the database.
10. Security for users: Options for editing, deleting and updating available bookings and food items are only shown when logged in as an admin user, not for general users or users without an account and there are failsafes in place should they navigate to these URLs manually, they won't see the options but if they do they will not be successful when changing data and will be redirected to the homepage.

I tested the speed of my website using the full page test in [Pingdom](https://tools.pingdom.com/) Tools.
This specific test was done on 29 November 2020. The web page took 968 ms to load, used 23 requests, and weighed in at 2.0 MB.
The Google Page Speed performance grade for this web page is 85/100.
More information on this test can be found [here](https://tools.pingdom.com/#5d853cbc71c00000)

I also tested for known vulnerabilities within my dependencies using [snyk](https://snyk.io/) and found that within all the dependencies used there are no known vulnerabilites. This means the website is secure with regards to the dependencies.

I also tested the code quality with [deepcode](https://www.deepcode.ai/). I made a couple of adjustments from the suggestions and now the code seems good quality, with no warnings, only one informational issue and 3 lint issues. More information can be found if you have a deepcode account [here]().

Screensizes and Devices:

- I tested the website to make sure it functioned correctly and displayed well on every device given using Chrome Developer Tools when viewing the site in a browser and also that it transitioned well when changing the screensize responsively from large to small.
- I tested the website on a number of browsers including chrome and firefox to make sure it functioned as expected on 
all of them. 
- I tested the website on different laptop types including Acer Chromebook, Dell Inspiron and a ThinkVision 4K external 
screen.
- I tested the website on a number of mobile devices to make sure it displayed correctly and worked as expected. These 
included a Samsung S20, Huawei p20, Samsung S7, iPhone 5s and a Samsung S8.

## Deployment

In order to deploy this website using Heroku I navigated to the app within Heroku. I then clicked on settings and scrolled down to domains. The URL is shown here with the link to the published app showing as https://eco-fitness.herokuapp.com/.

I have also linked the Github repo to the app in Heroku directly for continuous integration and deployment when editing the app.


In order to deploy the website locally you would need to go to the GitHub repository directly. You would then need to click download and copy the link that it gives you. Next go to your terminal, enter the directory you wish to clone it to using the cd 
command and then type git clone and paste in the link you just copied. You can then enter the website directory again 
using the cd command and ls will bring up a list of the files. These can then be opened in your choice of editor. You would then need to give your own environment variables for the variables within settings.py in order to deploy your own working version of the app.

## Credits

### Content
- The HTML used for the full page background was edited from [CSS-TRICKS, article ‘Perfect Full Page Background Image'](https://css-tricks.com/perfect-full-page-background-image/).
- I used a lot of inspiration and knowledge from [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma-uk/?utm_expid=.E_bf0H2MSRWB3VqLwMyfkg.1&utm_referrer=https%3A%2F%2Fcodeinstitute.net%2F5-day-coding-challenge%2F%3Futm_term%3Dcode%2520institute%26utm_campaign%3Da%252526c_BR_IRL_Code_Institute%26utm_source%3Dadwords%26utm_medium%3Dppc%26hsa_net%3Dadwords%26hsa_tgt%3Dkwd-319867646331%26hsa_ad%3D417883010334%26hsa_acc%3D8983321581%26hsa_grp%3D62188641240%26hsa_mt%3De%26hsa_cam%3D1578649861%26hsa_kw%3Dcode%2520institute%26hsa_ver%3D3%26hsa_src%3Dg%26gclid%3DCj0KCQiAqo3-BRDoARIsAE5vnaL9OoGIItwtIK8i3GmeQUkfe70hxCZKEzcjiPZJM5DhdwZtTbAJohMaAj1xEALw_wcB%26gclsrc%3Daw.ds) specifically the Boutique Ado project in order to complete this project. Some code has been used directly from this project.
