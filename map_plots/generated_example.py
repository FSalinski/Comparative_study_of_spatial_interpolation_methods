'''
Partially random geostatistical data generated
on [0, 1] x [0, 1] square. We generate random 100
points and assing value with the following formula:
z = 2 * x + y + np.random.normal(0, 1)
'''

import logging
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs


def generate_data(n_points=100):
    x = np.random.rand(n_points)
    y = np.random.rand(n_points)

    z = 2 * x + y + np.random.normal(0, 1, n_points)

    return pd.DataFrame({'x': x, 'y': y, 'z': z})


def plot_data(df, show=True):
    geo_df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y),
                              crs="EPSG:4326")

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw={'projection': ccrs.PlateCarree()})

    grid = ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    ax.set_title("Wygenerowane dane geostatystyczne")

    geo_df.plot(
        ax=ax,
        column='z',
        cmap='viridis',
        markersize=30,
        legend=True,
        legend_kwds={
            'label': 'Z',
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

    df = generate_data()
    logging.info(f"Generated data sample:\n{df.head()}")

    plot = plot_data(df, show=False)

    # Save plot to file
    plot[0].savefig("img/generated_example.png")


if __name__ == "__main__":
    main()
