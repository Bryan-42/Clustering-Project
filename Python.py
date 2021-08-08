from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import csv

rows = []

with open("final.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

star_masses = []
star_radiuses = []

for star_data in star_data_rows:
  star_masses.append(star_data[2])
  star_radiuses.append(star_data[3])

x = []

for index,star_mass in enumerate(star_masses):
  temp_list = [
    star_radiuses[index],
    star_mass
  ]
  x.append(temp_list)

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

plt.figure(figsize = (10,5))
sns.lineplot(range(1,11),wcss, marker = 'o', color = 'red')
plt.title("The Elbow Method")

plt.xlabel("Number of Clusters")
plt.ylabel("Wcss")

plt.show

star_masses = []
star_radiuses = []
star_gravities = []
for star_data in star_data_rows:
  star_masses.append(star_data[2])
  star_radiuses.append(star_data[3])
  star_gravities.append(star_data[4])

fig = px.scatter(x= star_radiuses, y = star_masses, color= star_gravities)
fig.show()