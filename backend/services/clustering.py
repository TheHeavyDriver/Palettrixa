from sklearn.cluster import KMeans
import numpy as np
from config import DEFAULT_CLUSTERS
from skimage.color import rgb2lab, lab2rgb


def extract_dominant_colors(pixels: np.ndarray):

    # normalize RGB values (0-1)
    pixels_normalized = pixels / 255.0

    # convert RGB → LAB
    lab_pixels = rgb2lab(pixels_normalized.reshape(-1, 1, 3)).reshape(-1, 3)

    # run clustering in LAB space
    kmeans = KMeans(n_clusters=DEFAULT_CLUSTERS, n_init=10)
    labels = kmeans.fit_predict(lab_pixels)

    centers_lab = kmeans.cluster_centers_

    # count cluster frequencies
    counts = np.bincount(labels)

    # sort clusters by dominance
    sorted_indices = np.argsort(counts)[::-1]

    sorted_lab_colors = centers_lab[sorted_indices]

    # convert LAB → RGB
    rgb_colors = lab2rgb(sorted_lab_colors.reshape(-1,1,3)).reshape(-1,3)

    rgb_colors = (rgb_colors * 255).astype(int)

    return rgb_colors