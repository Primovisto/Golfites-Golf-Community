<h1>Golfites Golf Community</h1>
This project is an ecommerce golfing marketplace and social community built using Django. The projects main features include:

1. User Registration, Login, Logout, Profile/Member dashboard.
2. Users Register as Golfites members on a subscription basis at €4.99/month.
2. Registered users can upload ads in order to sell their old golf equipment (Donedeal for Golfers).
3. Registered users can choose to Edit/Delete their uploaded ads.
4. Registered users can purchase equipment directly from Golfites via Paypal.
5. All users can access the sites academy to get the latest golfing hints and tip.
6. Registered users can create their own golfer social profile and browse other members profiles.
7. All users can access Golfites 'Course finder' to locate and get information on over 400 golf courses in Ireland.
8. Registered users can access the Golfites forum to chat with fellow members.

<h2>Hosting</h2>
A demo of the Golfites site is currently being hosted <a href="https://golfites-golf-community.herokuapp.com">here</a>

<h2>Built With</h2>
Django: A Python based web application framework for rapid development
<br>
sqlite3: a powerful, open source object-relational database system
<br>
Stripe: a web application that allows individuals and business to accept secure credit card payments on their website
<br>
HTML, CSS and JavaScript: Front end languages that give the application structure, style and interactivity

<h2>Deployment</h2>

If you would like to deploy this app locally download or clone this repo and follow the guideline below:

1. Install Python 3.6.3
2. Create and activate a local virtual environment
3. run pip install -r requirements.txt
4. Connect to your own database - Adjust database configurations in setting.py file and in virtual environment
5. Run:
<li>$python manage.py makemigrations</li>
<li>$python manage.py migrate</li>
<li>$python manage.py createsuperuser</li>

6. Run: 
<li>python manage.py runserver</li>

7. Finally, navigate to http://localhost:8000/ to view your app locally.

<h2>Author</h2>

Edward Stack - This project was completed as part of Code Institutes mentored online program.

<h2>Acknowledgements</h2>
Bootstrap, jQuery, Owl Carousel, animate.css, font-awesome, Heroku, Javascript