# Aprendizado-de-Máquina --- **PI2**

Este projeto contém dois modelos de aprendizado de máquina **não
supervisionado**, desenvolvidos para o Projeto Individual (PI2),
incluindo:

-   **K-Means**
-   **DBSCAN**

Ambos foram aplicados em um conjunto de dados (fictício) de clientes,
com o objetivo de realizar **agrupamento (clustering)** e identificar
padrões naturais nos dados.

------------------------------------------------------------------------

## 🛠️ 1. Preparando o ambiente

### ✔️ 1.1 Instale o Python

Versão recomendada: **Python 3.10 ou 3.11**\
Baixe em: https://www.python.org/downloads/

Durante a instalação, marque:

✔️ Add Python to PATH

------------------------------------------------------------------------

## 📂 2. Instalando as bibliotecas necessárias

Abra o terminal do VS Code e execute:

    pip install numpy pandas matplotlib seaborn scikit-learn

Essas bibliotecas são suficientes para rodar o K-Means e o DBSCAN, além
da geração de gráficos.

------------------------------------------------------------------------

## 📦 3. Estrutura de pastas sugerida

    PI2
    │─ KMeans_DBSCAN.py
    │─ README.md

------------------------------------------------------------------------

## ▶️ 4. Como rodar o código

1.  Abra o VS Code\
2.  Vá em **File \> Open Folder** e selecione a pasta do projeto\
3.  Abra o arquivo `.py` desejado\
4.  Vá em **Terminal \> New Terminal**\
5.  Execute:

```{=html}
<!-- -->
```
    python KMeans_DBSCAN.py

------------------------------------------------------------------------

## 🔵 5. Como rodar o arquivo K-Means + DBSCAN

**Arquivo:** `KMeans_DBSCAN.py`

    python KMeans_DBSCAN.py

Esse arquivo contém:

-   Importação e geração dos dados\
-   Processo de ETL e limpeza\
-   Aplicação do **K-Means**\
-   Aplicação do **DBSCAN**\
-   PCA para visualização\
-   Gráficos dos clusters\
-   Interpretação dos resultados no próprio terminal

------------------------------------------------------------------------

## 🎨 6. Visualização dos gráficos

O projeto utiliza matplotlib e seaborn, então:

-   Dois gráficos serão exibidos automaticamente:
    -   Clusters formados pelo K-Means\
    -   Clusters formados pelo DBSCAN\
-   A janela com o gráfico abre ao final da execução.

------------------------------------------------------------------------

## 🧠 7. Sobre os modelos utilizados

### **K-Means**

-   Clusters com formato esférico\
-   Rápido\
-   Necessita escolher k

### **DBSCAN**

-   Identifica clusters de formatos irregulares\
-   Detecta outliers\
-   Não precisa definir k\
-   Depende de eps e min_samples

------------------------------------------------------------------------
