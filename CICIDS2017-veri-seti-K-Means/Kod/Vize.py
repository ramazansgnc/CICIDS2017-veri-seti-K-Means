import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from ipaddress import ip_address

# 'Wednesday-workingHours.pcap_ISCX.csv' veri setini oku
file_path = "Wednesday-workingHours.pcap_ISCX.csv"
selected_features = [
    'Flow ID', 'Source IP', 'Destination IP', 'Timestamp', 'Label'
]

df = pd.read_csv(file_path, encoding='latin1', dtype=str, usecols=selected_features)

# 'Flow ID' sütununu sayısal bir indekse dönüştürür
df['Flow ID'] = df['Flow ID'].astype('category').cat.codes

# 'Source IP' ve 'Destination IP' sütunlarını sayısal değerlere dönüştürür
df[['Source IP', 'Destination IP']] = df[['Source IP', 'Destination IP']].applymap(lambda x: int(ip_address(x)) if pd.notna(x) else x)

# Seçilen nitelikleri sayısal türlere çevirir
df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors='coerce')

# Eksik değerleri sıfır ile doldurur
df = df.fillna(0)

# K-Means için sadece gerekli sütun
features_for_kmeans = df.drop(['Label'], axis=1)

# K-Means algoritmasını uygular
kmeans = KMeans(n_clusters=6, random_state=0)
kmeans.fit(features_for_kmeans)

# Küme merkezlerini ve örnekleri görselleştirmek için boyut indirgeme (PCA) kullanıldı
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(features_for_kmeans)

# Küme merkezleri ve örnekleri çizildi
plt.figure(figsize=(10, 6))
scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.legend(*scatter.legend_elements(), title="Clusters")
plt.title('K-Means Clustering for H.csv')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
