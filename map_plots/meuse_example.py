'''
Example of a geostatistical data
using the Meuse dataset.
'''

import logging
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs


URL = "https://raw.githubusercontent.com/filipkral/meuse/refs/heads/master/meuse.txt"


def load_meuse_data(url):
    return pd.read_csv(url)


def plot_meuse_data(df, show=True):
    geo_df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y),
                              crs="EPSG:28992")
    

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw={'projection': ccrs.epsg(28992)})

    grid = ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    grid.top_labels = False
    grid.right_labels = False
    ax.set_title("Poziom stężenia cynku, dane Meuse")

    geo_df.plot(
        ax=ax,
        column='zinc',
        cmap='viridis',
        markersize=20,
        legend=True,
        legend_kwds={
            'label': 'Zinc',
            'orientation': 'horizontal',
            'shrink': 0.8,
            'pad': 0.05
        }
    )

    # Cut off white space
    plt.tight_layout(pad=1)

    if show:
        plt.show()
        
    return fig, ax


def main():
    # Set directory to working file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    logging.basicConfig(level=logging.INFO)

    np.random.seed(42)

    df = load_meuse_data(URL)
    logging.info(f"Loaded Meuse dataset sample: {df.head()}")

    plot = plot_meuse_data(df, show=True)

    # Save plot
    plot[0].savefig('img/meuse_example.png')
    

if __name__ == '__main__':
    main()
