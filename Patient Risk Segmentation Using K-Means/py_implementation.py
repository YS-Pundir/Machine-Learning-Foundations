# step 0 : importing the tools
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


#step 1 : Loading the data
print("_"*100)   

np.random.seed(42)

data = {
    'systolic_bp':   np.concatenate([np.random.normal(118, 10, 150),
                                     np.random.normal(142, 12, 150),
                                     np.random.normal(168, 8,  100)]),
    'cholesterol':   np.concatenate([np.random.normal(178, 18, 150),
                                     np.random.normal(222, 22, 150),
                                     np.random.normal(262, 18, 100)]),
    'bmi':           np.concatenate([np.random.normal(21.5, 2, 150),
                                     np.random.normal(27.0, 3, 150),
                                     np.random.normal(33.5, 3, 100)]),
    'glucose_level': np.concatenate([np.random.normal(88,  10, 150),
                                     np.random.normal(112, 14, 150),
                                     np.random.normal(148, 18, 100)]),
    'age':           np.concatenate([np.random.normal(34, 7,  150),
                                     np.random.normal(51, 6,  150),
                                     np.random.normal(63, 5,  100)])
}

df_orignal  = pd.DataFrame(data)
#making the copy of original dataframe
df=df_orignal.copy()





# Step 2 : appling the Principal Component Analysis . to data to compress the  features to 2 peremeters only
    
    # Scaling the data
scaler=StandardScaler()
df=scaler.fit_transform(df)
df=pd.DataFrame(df,columns=['systolic_bp','cholesterol','bmi','glucose_level','age'])
print("--------","Scaled Data Without PCA","--------")
print(df)

    # Appling the Principle Component Analysis
pca=PCA(n_components=2)
df=pca.fit_transform(df)
df=pd.DataFrame(df,columns=["Principle Component 1","Principle Component 2"])
print("--------","Scaled Data With PCA","--------")
print(df)


# step 3 : Finding the optimal K 
wcss=[]
for k in range(1,15):
    kmeans=KMeans(n_clusters=k,init="k-means++",random_state=42)
    kmeans.fit(df)
    inertia=kmeans.inertia_
    wcss.append(inertia)

    # Plotting the graph of k v/s wcss
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(range(1,15),wcss,marker="o",linestyle="--")
plt.xlabel("Number of Clusters")
plt.ylabel("Amount of Inertia")
plt.title("Elbow Method — Optimal K for Patient Clustering")




# step 4 : training the actual KMEans model
print()
print("_"*100)
kmeans=KMeans(n_clusters=3,init="k-means++",n_init=10,random_state=42)
kmeans.fit(df)
labels=kmeans.predict(df)

plt.subplot(1,2,2)
plt.scatter(df["Principle Component 1"],df["Principle Component 2"],c=labels,cmap="viridis",s=50)
center=kmeans.cluster_centers_
plt.scatter(center[:,0],center[:,1],c="red",marker="X",label="Centroid")
plt.legend()
plt.xlabel("Principle Component 1")
plt.ylabel("Principle Component 2")
plt.title("Clustered data")




# step 5 : printing the summary table 

print("--------","Summary Table","--------")
df_orignal["Cluster"]=kmeans.labels_

summary_table=df_orignal.groupby("Cluster").mean()
print(summary_table)
plt.show()