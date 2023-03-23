# project1-mauro-alvizo
# H1 READ ME for project1
# H2 By Mauro Alvizo

# H3 Technology Used
This web app used Flask and Python to create a movie learning experience.
I used the TMDB API and the Wikipedia API

I used flask to construct the server, css to format the HTML and make things look pretty.
I also constructed buttons that used flask to redirect back and forth an about page for fun
A little bit of python and CSS were used to make the background colors change on refresh which I did because I thought it would look cooler.

I used a container to create a primitive toolbar for the site

# H3 How to implement if forked

If you decide to fork this project and use it to deploy your own service you would download all the files into a folder on your computer and then
ensure the requirements.txt and Procfile are properly formatted to you system. You would then have to setup fly on your own device. I reccommend following
the [fly.io tutorial to set this up.](https://fly.io/docs/languages-and-frameworks/python/) You would follow those steps until you are able to launch your own
version of my website.

# H3 What I struggled with

Everything was relatively easy except for my time management and deploying to fly. My time management was not that bad because I still managed to finish well before the deadline but in the future I want to give myself more time to add more creative things because it was really fun. Deploying to fly was a different story I struggled so much with it. My main problem was that for some reason my WSL would not build the deployable correctly. So to solve that I had to go to fly's free command line online to deploy. Then I ran into Missing Module problems that stemmed from my incorrect requirements file which I had a classmate help me figure out.

# H3 2 Known Problems

The first problem is that I am not sure entirely how it's working without me putting an API key in the secrets tab. I have no clue how it's able to fetch things. I didnt leak my key either because I had to comment out the lines correlating to dotenv files so the biggest problem is that I dont understand how it's working at it's current capacity.

My second current problem is that I wanted to spend more time making it look pretty but I ran out of time because I procrastinated. My b. I am still proud of how it turned out though and it was a really fun project minus deployment.


