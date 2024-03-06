import os
import umap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from umap import UMAP
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class DimensionalityReducer(object):

    def __init__(self, data_filename: str, target: str = 'Target'):

        # data filename to store CSV
        self.data_filename = data_filename

        # set target name
        self.target_name = target

        # dataframe to store reading data
        self.data = self.read_data()
        print(f'Size of the dataset: {self.data.shape}')

        # get target from dataframe
        self.target = self.data[self.target_name]
        print(f'Target shape: {self.target.shape}')

        # lets drop the target column now
        self.data = self.data.drop([self.target_name], axis=1)

        return

    def read_data(self) -> pd.DataFrame:
        # What happens if the file does not exist?
        # Hint: assert and check the file existance
        assert os.path.exists(self.data_filename), \
            f'{self.data_filename} from argument -d does not exist.'
        df = pd.read_csv(self.data_filename)
        return df

    def sample_data(self, sample_value: int):
        self.data = self.data.sample(sample_value, random_state=2)
        self.target = self.target[self.data.index]
        return

    def normalize_data(self):
        scaler = StandardScaler()
        self.data = scaler.fit_transform(self.data)
        return

    def reduce_with_pca(self, n_components: int = 2):
        pca = PCA(n_components=n_components)
        reduced_data = pca.fit_transform(self.data)
        return reduced_data

    def reduce_with_tsne(self, n_components: int = 2, perplexity: float = 30.0):
        tsne = TSNE(n_components=n_components, perplexity=perplexity, random_state=42)
        reduced_data = tsne.fit_transform(self.data)
        return reduced_data

    def reduce_with_umap(self, n_components: int = 2):
        umap = UMAP(n_components=n_components)
        reduced_data = umap.fit_transform(self.data)
        return reduced_data

    def plot_reduced_data(self, reduced_data, target, title='Reduced Data'):
        plt.figure(figsize=(10, 8))

        # TODO: consider adding more dynamic colors depending on the size
        # of target values
        colors = [
            'red', 'green', 'blue', 'cyan', 'magenta',
            'yellow', 'black', 'purple', 'lime', 'navy'
        ]
        for i in range(len(colors)):
            plt.scatter(
                reduced_data[target == i, 0],
                reduced_data[target == i, 1],
                c=colors[i],
                label=str(i),
                alpha=0.6  # things like this can go as arguments
            )
        plt.title(title)
        plt.legend()
        plt.xlabel('Component 1')
        plt.ylabel('Component 2')
        plt.show()
        return
