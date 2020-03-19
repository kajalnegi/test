import numpy as np
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def k_means(X,k=2):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    label = kmeans.labels_
    sil_coeff = silhouette_score(X, label, metric='euclidean')
    return sil_coeff, label


def select_k(gap):
    k = min(gap.keys())
    return k


def calculate_gap(sil_score):
    gap = dict()
    for k,v in sil_score.items():
        if k >= 3:
            if sil_score[k - 1] - sil_score[k] > 0:
                gap[k] = sil_score[k - 1] - sil_score[k]
    return gap


def k_labels(X):
    sil_score = dict()
    labels = dict()
    for k in range(2,len(np.unique(X))):
        sil_coeff, label = k_means(X,k=k)
        sil_score[k] = sil_coeff
        labels[k] = label
        #print(k)
        #print(labels)
    gap = calculate_gap(sil_score)
    final_k = select_k(gap)
    return final_k, labels[final_k]

