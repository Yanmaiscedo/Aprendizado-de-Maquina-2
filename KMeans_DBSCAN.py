# ================================================
# PROJETO PI2 - K-Means e DBSCAN
# Agrupamento de Clientes
# ================================================

# --- IMPORTAÇÕES ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
import seaborn as sns

# Para deixar os gráficos mais bonitos
sns.set(style="whitegrid")

# ------------------------------------------
# 1) GERAÇÃO / IMPORTAÇÃO DOS DADOS (ETL)
# ------------------------------------------
# Criando dados fictícios de clientes
np.random.seed(42)

n = 300
idades = np.random.normal(35, 10, n).clip(18, 65)
rendas = np.random.normal(5000, 2000, n).clip(1200, 15000)
gastos = np.random.normal(800, 300, n).clip(100, 3000)
frequencia = np.random.normal(12, 5, n).clip(1, 40)

df = pd.DataFrame({
    "idade": idades,
    "renda": rendas,
    "gasto_medio": gastos,
    "frequencia": frequencia
})

print("Prévia dos dados:")
print(df.head())

# ------------------------------------------
# 2) LIMPEZA DOS DADOS
# ------------------------------------------
# Verificar valores nulos
print("\nValores nulos:")
print(df.isnull().sum())

# Escalonamento
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# ------------------------------------------
# 3) REDUÇÃO DE DIMENSIONALIDADE PARA GRÁFICOS
# ------------------------------------------
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

# Colocar em DataFrame para facilitar gráficos
df_plot = pd.DataFrame(df_pca, columns=["PC1", "PC2"])

# --------------------------------------------------------
# 4) MODELO 1: K-MEANS
# --------------------------------------------------------
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
clusters_kmeans = kmeans.fit_predict(df_scaled)

df_plot["cluster_kmeans"] = clusters_kmeans

# --- Gráfico do K-Means ---
plt.figure(figsize=(8,6))
sns.scatterplot(x="PC1", y="PC2", hue="cluster_kmeans",
                palette="viridis", data=df_plot, s=60)
plt.title("Clusters formados pelo K-Means")
plt.show()

# --------------------------------------------------------
# 5) MODELO 2: DBSCAN
# --------------------------------------------------------
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters_db = dbscan.fit_predict(df_scaled)

df_plot["cluster_dbscan"] = clusters_db

# --- Gráfico do DBSCAN ---
plt.figure(figsize=(8,6))
sns.scatterplot(x="PC1", y="PC2", hue="cluster_dbscan",
                palette="tab10", data=df_plot, s=60)
plt.title("Clusters formados pelo DBSCAN")
plt.show()

# --------------------------------------------------------
# 6) ANÁLISE DE RESULTADOS
# --------------------------------------------------------
print("\nQuantidade de clusters (K-Means):", len(np.unique(clusters_kmeans)))
print("Clusters encontrados pelo K-Means:", np.unique(clusters_kmeans))

print("\nQuantidade de clusters (DBSCAN):", len(np.unique(clusters_db)))
print("Clusters encontrados pelo DBSCAN:", np.unique(clusters_db))

# Estatísticas dos grupos do K-Means
df["cluster"] = clusters_kmeans
print("\nMédias por cluster (K-Means):")
print(df.groupby("cluster").mean())
