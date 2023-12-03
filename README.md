# NRDY 🎵 
NRDY is a content and collaborative based song recommender.

# Song-Recommender-cosine-similarity-and-KNN
[Colab Notebook](https://colab.research.google.com/drive/1vbPJnJIXYUzoC8RfQ8QfvSbg5S6v7nKS#scrollTo=ppWlDR9njTb5)
A song recommender using Spotify data based on two approaches - "Content-based recommendation" that uses TFIDF and cosine similarity and "Collaborative Filtering based recommendation" that uses KNN (K-nearest neighbors) classification model. For content based filtering, we find similarity based on song name, album, artist and release date, whereas for collaborative filtering, we consider numeric features like accousticness, popularity, danceability, etc.

# Steps to Run:
- python3 -m pip install -r requirements.txt
- python3 app.py

- Home Screen: <br>
<img width="1435" alt="Screenshot 2023-09-29 at 11 45 33 AM" src="https://github.com/rashi-bhansali/Song-Recommender-cosine-similarity-and-KNN-/blob/main/Screenshots/Screenshot%202023-09-29%20at%2011.45.33%20AM.png"><br>

- Content-based Recommendations <br>
A. Based on Song Name<br>
<img width="1412" alt="Screenshot 2023-09-29 at 12 43 07 PM" src="https://github.com/rashi-bhansali/Song-Recommender-cosine-similarity-and-KNN-/blob/main/Screenshots/Screenshot%202023-09-29%20at%2012.43.07%20PM.png"><br>
B. Based on Artist<br>
<img width="1364" alt="Screenshot 2023-09-29 at 12 44 23 PM" src="https://github.com/rashi-bhansali/Song-Recommender-cosine-similarity-and-KNN-/blob/main/Screenshots/Screenshot%202023-09-29%20at%2012.44.23%20PM.png"><br>
C. Based on Release Date<br>
<img width="1388" alt="Screenshot 2023-09-29 at 12 44 13 PM" src="https://github.com/rashi-bhansali/Song-Recommender-cosine-similarity-and-KNN-/blob/main/Screenshots/Screenshot%202023-09-29%20at%2012.44.13%20PM.png"><br>
- Collaborative Filter based Recommendations <br>
<img width="1422" alt="Screenshot 2023-09-29 at 12 09 19 PM" src="https://github.com/rashi-bhansali/Song-Recommender-cosine-similarity-and-KNN-/blob/main/Screenshots/Screenshot%202023-09-29%20at%2012.09.19%20PM.png"><br>



