import matplotlib.pyplot as plt
import pandas as pd

# Read the file bechdelExpanded.csv with pandas
df = pd.read_csv("bechdelExpanded.csv")

# Learn about your data with .head() and .info()
df.head()
print(df.info())

# Data Manipulation: Create a column for total_score and set the value of each of its entries equal to the sum of the columns: bechdel, waithe, ko
df["total_score"] = df.bechdel + df.waithe + df.ko
df.head()

# Sorting Data: organize your data and reset the index of the new DataFrame using .reset_index(drop = True)
df_sorted = df.sort_values("total_score").reset_index(drop=True)
df_sorted.head()

# Isolating the data: create a new DataFrame containing only the columns 'movie', 'bechdel', 'waithe', 'ko', 'total_score' from the df_sorted DataFrame
df_goodata = df_sorted[["movie", "bechdel", "waithe", "ko", "total_score"]]
df_goodata.head()

# Plot DataFrame with Matplotlib
# Using [[]] notation, select the columns movie and total_score from the DataFrame df_partial, then using .set_index(), set the index to the columns movie, and save it all to a variable named ax
ax = df_partial[['movie', 'total_score']].set_index('movie') 
# Create a plot of the ax DataFrame with the Matplotlib method .plot(). Include the following arguments inside of .plot() . You can change these on your own and run the plot again if you would like.
# kind = 'bar'; title ='Representation In Movies'; figsize=(15, 10); legend=True
ax.plot(kind='bar', title ='Representation In Movies', figsize=(15, 10), legend=True)

# Iterate and Discover Meaning: kind=barh, fontsize=12, figsize=(15,15)
ax.plot(kind='barh', title ='Representation In Movies', figsize=(15, 15), legend=True, fontsize=12)