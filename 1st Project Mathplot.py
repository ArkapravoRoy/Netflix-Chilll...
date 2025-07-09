
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\NeelLaptop\Desktop\Python\Netflix Dataset export 2025-07-01 11-43-24.csv")

df.dropna(subset=["type","release_year","rating","country","duration"])

count=df['type'].value_counts()# counting movies vs tv shows
plt.bar(count.index,count.values,color=["skyblue","orange"])

plt.title("Number of TV shows vs Movies on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Netflix1.png")
plt.show()

ratcnt=df['rating'].value_counts()#counts the rating of Movies
plt.pie(ratcnt,autopct="%.1f%%",labels=ratcnt.index, startangle=90)

plt.title("Percentage of Contend Rating")
plt.tight_layout()
plt.savefig("Contend_Rating.png")
plt.show()

# mvdf=df[df["type"]=='Movie'].copy()
# mvdf["duration_int"] = mvdf['duration'].str.replace(' min', '', regex=False).astype(int)


# plt.hist(mvdf['duration_int'],bins=30,color="red",edgecolor="black")

# plt.title("Movies Duration")
# plt.xlabel("Duration of Time(minutes)")
# plt.ylabel("Duration of Movies")
# plt.tight_layout()
# plt.savefig("Movie duration.png")
# plt.show()
mvdf = df[(df["type"] == 'Movie') & (df['duration'].str.contains('min', na=False))].copy()
mvdf["duration_int"] = mvdf['duration'].str.replace(' min', '', regex=False).astype(int)

# Plot histogram
plt.hist(mvdf['duration_int'], bins=30, color="red", edgecolor="black")
plt.title("Movies Duration")
plt.xlabel("Duration of Time (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("movie_duration.png")
plt.show()

#Creating scatter plot

recount=df['release_year'].value_counts().sort_index()

plt.scatter(recount.index,recount.values, color="purple")
plt.title("Release Years vs No of Shows ")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.savefig("Release_year.png")
plt.show()

#Printing Top 10 countries with maximum number of shows

cc=df["country"].value_counts().head(10)

plt.bar(cc,cc.index,cc.values,color="teal")

plt.title("Top 10 countries with maximum number of shows ")
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("Top10 coutry.png")
plt.show()
