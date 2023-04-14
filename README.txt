RECOMMENDATION SYSTEM


Run of Web Application:
* We used anaconda prompt to host our web application.
* Go to the location of the project folder.
* Run the command “streamlit run  ./app.py”.
Design :
* Firstly we can see hading Recommendation System
* There is a dropdown that has both Movies and Books options.
* When Books is selected Book Recommendation System is displayed below. Same goes with movies also.
* The default is set to movies here.
Files:
* App code is present in app.py
* For multiple applications in a single streamlit app, we used multipleapp.py
* The multiple apps are present in apps folder
* The movies app requires 3 files. Movies python file for running streamlit app, movies.pkl and similarity.pkl , The recommendation system code is present in Movie Recommendation System.ipynb
* Books app requires 3 files i.e Books-.py file for running streamlit app, books.pkl,similarity_b.pkl, The recommendation system code is present in Book Recommendation System.ipynb
* Movies.pkl, books.pkl has the data frames downloaded from .ipynb file to load in the app
* Similarity.pkl and similarity_b.pkl has the cosine similarity arrays saved to show the recommendation of movie and books.