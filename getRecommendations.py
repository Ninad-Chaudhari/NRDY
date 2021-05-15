import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from tfidf import TFIDF

def getRecommendation(new_df, record):
    temp_df = new_df[['id','name', 'album', 'artist', 'release_date']]
    temp_df = pd.concat([temp_df, record], ignore_index = True)
    
    col = ['name', 'album', 'artist', 'release_date']
    data = pd.DataFrame(columns=col)
    id = []
    for i in col:
        yield "<br/>"
        tf = TFIDF(temp_df, i)
        cosine_sim = linear_kernel(tf, tf) 
        data[i] = cosine_sim[-1]
        d1 = data.sort_values(by=[i], ascending=False)
        id.append(list(d1.head(7).index))
    
    tid = []
    for i in range(4):
        track_id = []
        for j in id[i]:
            track_id.append(temp_df.iloc[j, 0]) 
        tid.append(track_id)
    return tid 
