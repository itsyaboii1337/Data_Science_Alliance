
# Helpers functions for plotting
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from fuzzywuzzy import process


#Some constants for colors and theme
COLOR_SCALE = "Reds"
MARKER_LINE_COLOR = "white"
THEME = "plotly_white"
MARKER_LINE_WIDTH = 0.5

def slider_map(df, z_col_name, title, country_col_name = 'country', zmin = 0, zmax = 10,  year_col = 'Year' , location_col_name ='Code' ):
    """Plot dynamic maps with slider for years

    Parameters
    ----------
    df : The dataframe. The year must contain only numeric values.
    z_col_name : Name of the column containg the data.
    title : Title of the map
    country_col_name : Name of rhe colum with the contry names
    zmin : Minimum value of the data
    zmax : Maximum value of the data
    year_col : Name of the colum containing the years
    location_col_name : Name of the column containg the country codes

    """
    data_slider = []
    years = sorted(df[year_col].unique())
    for year in sorted(df[year_col].unique()):


        # I select the year (and remove DC for now)
        df_year = df[(df[year_col]== year )]

        ### create the dictionary with the data for the current year
        data_one_year = dict(
                            type='choropleth',
                            locations = df_year[location_col_name],
                            z=df_year[z_col_name],
                            zmin=zmin,
                            zmax = zmax,
                            colorscale = COLOR_SCALE,
                            autocolorscale=False,
                            reversescale=False,
                            marker_line_color= MARKER_LINE_COLOR,
                            marker_line_width=MARKER_LINE_WIDTH,
                            text = df_year[country_col_name],
                            colorbar_title= title ,
                            )

        data_slider.append(data_one_year)  # I add the dictionary to the list of dictionaries for the slider
    ##  I create the steps for the slider

    steps = []

    for i in range(len(data_slider)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data_slider)],
                    label='Year {}'.format(years[i])) # label to be displayed for each step (year)
        step['args'][1][i] = True
        steps.append(step)


    ##  I create the 'sliders' object from the 'steps'

    sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

    # I set up the layout (including slider option)


    # I create the figure object:

    fig = go.Figure(data=data_slider)

    # to plot in the notebook

    #plotly.offline.iplot(fig)
    fig.update_layout(geo=dict(showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'),
        sliders=sliders,
        template=THEME
    )
    fig.show()
    return fig


def match_names(countryNames, countryNames2, similarity_limit=65):
    countryNames = np.unique(countryNames)
    countryNames2 = np.unique(countryNames2)
    missingPair = np.setdiff1d(countryNames, countryNames2)
    missingPairs2 = np.setdiff1d(countryNames2, countryNames)
    pairs = []
    similarities = []
    for name in missingPair:
        pair, similairity = process.extractOne(name, missingPairs2)
        pairs.append(pair)
        similarities.append(similairity)
    for i in range(len(pairs)):
        pairDf = pd.DataFrame({'Country': missingPair, 'Replacement': pairs, 'Similarity': similarities})
        noFound = pairDf[pairDf['Similarity'] <= similarity_limit]
        print("No matches found for:")
        for name in noFound["Country"]:
            print(name)
        pairDf = pairDf[pairDf['Similarity'] > similarity_limit]
        pairDf = pairDf.reset_index(drop=True)
    return pairDf


def replace_names(df, old, new):
    dfNew = df.replace(list(old.values), list(new.values))
    for i in range(len(new)):
        print("Replaced", old[i], "with", new[i])
    return dfNew
