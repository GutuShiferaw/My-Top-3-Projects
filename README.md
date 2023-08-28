# My-Top-3-Projects
## This is a selection of my three best projects.
1. The first project is a Game prediction App i made by training a machine learning Model. I worked on this project when i took my AI course, I was thinking of a way i could implement what i learnt on a real life application.I Created this App by training a Gradient Boosting Machine learning model over a huge FiFa Data set. The App is  a basic Pyhton UI made using the tkinter pyhton modlue and it predicts soccer match outcomes betweeen two teams. 
2. The Second project is an application to control an LED light using a Raspberry Pi and a locally hosted Django server.
    Rough code structure is as follows
    piSensor.py - Python code to be ran on the Pi to control the LED and handle the photoresistor. The PIN variables can be changed to any valid GPIO pin if needed.
   
    manage.py - Main starting place of Django, used to run the server itself.
   
    urls.py (mysite) - Initial urls.py used to control URL patterns. /admin leads to the site's admin panel, while the home root refers to the URL pattern described in myapi's urls.py.
   
    views.py - Initialize the views and viewsets used in the application. Mode/Serial ViewSet classes are used to grab all their related objects and serialize them. The control method is where the main logic is     handled. It initializes the auth needed for the API, and updates the API if the request contains POST variables. Context is then pulled from the first Mode and State then served to the control template.
   
    control.html - Used to serve the actual control page to the user, UI could definitely be improved but it serves proper functionality. Uses a single form that posts to itself and uses two sets of radio buttons to control the mode (auto/manual) and state (on/off) of the light.
   
    urls.py (myapi) - Controls the URL patterns related to API and control functionality. Uses a router to properly serve the mode and state API pages.
   
    serializers.py - Definition of serializers used to return Mode and State objects in a simpler to process form.
   
    models.py - Setting up simple classes for Mode and State, both only containing one field for the name and one overwritten function to return its own name when cast as a string.
   
   The reason why I worked on this project was to make use of the knowledge i have on embeded devices and cloud prpgramming to make a product that can be used for multpile purposes. 

