# Group comments by email, count comments
# Save to comments.csv
# Retreives comment data from API, converts it into a Pandas Dataframe.
import requests
import pandas as pd
response = requests.get("https://jsonplaceholder.typicode.com/comments")

# Checks for error in API 
response.raise_for_status()

# Converts JSON formatted comments into Python data
data = response.json()

# Converts the Python data into Data Frames (columns, rows)
df = pd.DataFrame(data)


try:
    # Groups together rows containing the same email 
    # .size() counts how many comments belong to each email
    #.reset_index(name = "new index name") is just a way of renaming the key of the index
    comment_counts = df.groupby("email")["id"].count().reset_index(name="comment_count")

    # Creates a csv file containing the grouped results
    comment_counts.to_csv("comments.csv")

   # Catches any errors from try  and prints explanation instead of crashing
except Exception as e:
    print ("An error occured:", e)

