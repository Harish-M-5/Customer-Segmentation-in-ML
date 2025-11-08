import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'CustomerID': [1,2,3,4,5,6,7,8,9,10],
    'Age': [19,21,20,23,31,45,40,60,65,70],
    'Annual_Income': [15000,18000,20000,24000,30000,60000,80000,100000,120000,150000],
    'Spending_Score': [80,76,60,65,50,40,30,20,15,10]
}

df = pd.DataFrame(data)

X = df[['Age', 'Annual_Income', 'Spending_Score']]

inertia = []
for k in range(1, 6):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.plot(range(1,6), inertia, marker='o')
plt.title('Customer Segmentation')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

plt.scatter(df['Age'], df['Spending_Score'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation')
plt.show()

print(df)
