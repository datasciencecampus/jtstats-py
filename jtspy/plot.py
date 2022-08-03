import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.lines import Line2D
import matplotlib as mpl
import math
import numpy as np
from descartes import PolygonPatch
import contextily as ctx


def create_grouped_scatter_plot(df, key1, key2, key3, title = None, figsize = (10,10), export_path = None, fmt = 'pdf', dpi = 300):
    '''
    

    Parameters
    ----------
    df : pandas dataframe
        Dataframe containing the data to plot.
    key1 : string
        Name of column to plot on x axis..
    key2 : string
        Name of column to plot on y axis.
    key3: string
        Name of column to use for grouping.
    title : string, optional
        Title of the plot. The default is None.
    figsize : tuple, optional
        Figure size (x,y). The default is (10,10).
    export_path : string, optional
        Path to save the file. The default is None.
    fmt : string, optional
        Format of the plot to save. The default is 'pdf'.
    dpi : integer, optional
        Resolution (dpi) of figure. The default is 300.

    Returns
    -------
    fig : matplotlib figure object
        Figure object. Only returned if export_path is None.

    '''
    
    fig = plt.figure(figsize = figsize)
    ax = fig.add_subplot(111)
    
    if title != None:
        plt.title(title, fontweight="bold", fontsize=16)
    
   
    # handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=v, label=k, markersize=20) for k, v in colors.items()]
    
    scatter = ax.scatter(x = df[key1], y = df[key2], c = df[key3])
    legend = ax.legend(*scatter.legend_elements())
    ax.add_artist(legend)
    
    # ax.legend(title='', handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left', prop = {'size':40})
    
    if export_path == None:
        
        return fig
    
    else:
        
        plt.savefig(export_path, format = fmt, dpi = dpi)
        
        


def create_scatter_plot(df, key1, key2, title = None, figsize = (10,10), export_path = None, fmt = 'pdf', dpi = 300):
    '''
    

    Parameters
    ----------
    df : pandas dataframe
        Dataframe containing the data to plot.
    key1 : string
        Name of column to plot on x axis..
    key2 : string
        Name of column to plot on y axis.
    title : string, optional
        Title of the plot. The default is None.
    figsize : tuple, optional
        Figure size (x,y). The default is (10,10).
    export_path : string, optional
        Path to save the file. The default is None.
    fmt : string, optional
        Format of the plot to save. The default is 'pdf'.
    dpi : integer, optional
        Resolution (dpi) of figure. The default is 300.

    Returns
    -------
    fig : matplotlib figure object
        Figure object. Only returned if export_path is None.

    '''
    
    
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    
    if title != None:
        plt.title(title, fontweight="bold", fontsize=16)
    
    ax.scatter(df[key1], df[key2])
    
    if export_path == None:
        
        return fig
    
    else:
        
        plt.savefig(export_path, format = fmt, dpi = dpi)


def choropleth_map(gdf, gdfval, outpath=None, fmt="pdf",
                    figsize=(8,8), title=None, valrange=[], logscale=False,
                    colormap="RdBu", cblabel=None, cbticks=None, cbticklabels=None,
                    tiles=None, dark_theme=False, linewidth=0.05, dpi=300, alpha = 1):
    """
    Plots a choropleth map given by GeoPandas object and values from a DataFrame.

    Parameters
    ----------
    gdf : GeoPandas DataFrame (Shapefile).
    gdfval : Field on df with values to plot.
    outpath : Output path. If None returns figure object.
    fmt : format of the plot.
    figsize : Figure size (x,y).
    title: Title of the plot.
    valrange : [min,max] range for the plot.
    logscale : If True plots logscale.
    colormap : Colormap in the maplotlib code reference.
    cblabel : Color bar label.
    cbticks : Colorbar ticks.
    cbticklabels : Labels for ticks in the color bar.
    tiles : Url for background tiles. Couple of examples are
                - 'https://a.basemaps.cartocdn.com/dark_all/tileZ/tileX/tileY.png'
                  (Dark map from CartoDB)
                - 'http://tile.stamen.com/terrain/tileZ/tileX/tileY.png'
                  (Street Map)
                If None, no background is used
    dark_theme : If True sets the text of labels in white and background in black.
    linewidth : Width of the borders of the polygons.
    dpi : Density of pixels.

    Output
    ------        
    If outpath is None returns the matplotlib figure object.
    
    """
    
    if dark_theme:
        plt.rcParams.update({
            "lines.color": "white",
            "patch.edgecolor": "white",
            "text.color": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "lightgray",
            "axes.labelcolor": "white",
            "xtick.color": "white",
            "ytick.color": "white",
            "grid.color": "lightgray",
            "figure.facecolor": "black",
            "figure.edgecolor": "black",
            "savefig.facecolor": "black",
            "savefig.edgecolor": "black"})

    if tiles != None:
        # Convert to Web Mercator coordinates
        gdf = gdf.to_crs(epsg=3857)

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    
    if title != None:
        plt.title(title, fontweight="bold", fontsize=16)
    
    plt.axis('off')
    
    # Bounding the map
    minx, miny, maxx, maxy = gdf["geometry"].unary_union.bounds
    w, h = maxx - minx, maxy - miny
    ax.set_xlim(minx - 0 * w, maxx + 0 * w)
    ax.set_ylim(miny - 0 * h, maxy + 0 * h)
    ax.set_aspect(1)
    
    if len(valrange) != 2:
        valrange = [gdf[gdfval].min(), gdf[gdfval].max()]
    
    # Plotting patches
    cmap = plt.get_cmap(colormap)
    patches = []

    for i,row in gdf.iterrows():
        
        val = row[gdfval]
        geom = row["geometry"]
               
        if(math.isnan(val)):
            
            if dark_theme:
                colour = "black"
            else:
                colour = "gainsboro"

            if tiles == None:
                alpha = 1
            else:
                alpha = 0
        else:
            if logscale:
                val = np.log10(val)
                normval = (val - np.log10(valrange[0])) / (np.log10(valrange[1]) - np.log10(valrange[0]))
                colour = cmap(normval)
            else:
                normval = (val - valrange[0]) / (valrange[1] - valrange[0])
                colour = cmap(normval)
            
            if normval < 0:
                normval = 0
            elif normval > 1:
                normval = 1
            
            if tiles == None:
                alpha = 1
#            else:
#                alpha = normval
        
        if geom.geom_type == "MultiPolygon":
            for pol in geom:
                patches.append(PolygonPatch(pol, fc=colour, alpha=alpha, ec='black', linewidth=linewidth))
        elif geom.geom_type == "Polygon":
            patches.append(PolygonPatch(geom, fc=colour, alpha=alpha, ec='black', linewidth=linewidth))
        else:
            patches.append(PolygonPatch(geom, fc=colour, alpha=alpha, ec='black', linewidth=linewidth))

    ax.add_collection(PatchCollection(patches, match_original=True))
    
    # Colorbar
    ax1 = fig.add_axes([0.22, 0.08, 0.60, 0.02])
    cmap2 = plt.get_cmap(colormap)
    
    if logscale:
        norm = mpl.colors.LogNorm(vmin=valrange[0], vmax=valrange[1])
    else:
        norm = mpl.colors.Normalize(vmin=valrange[0], vmax=valrange[1])
        
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap2, norm=norm, orientation='horizontal')
    
    if cblabel != None:
        cb1.set_label(cblabel)
    else:
        cb1.set_label(gdfval)
        
    if cbticks != None:
        cb1.set_ticks(cbticks)
        
    if cbticklabels != None:
        cb1.set_ticklabels(cbticklabels)
    
    if tiles != None:
        zoom=10
        
        xmin, xmax, ymin, ymax = ax.axis()
        basemap, extent = ctx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom, url=tiles)
        ax.imshow(basemap, extent=extent, interpolation='bilinear')
        # restore original x/y limits
        ax.axis((xmin, xmax, ymin, ymax))

    
    if outpath == None:
        return fig
    else:
        plt.savefig(outpath, format=fmt, alpha=True, dpi=dpi, bbox_inches='tight')
        mpl.rcParams.update(mpl.rcParamsDefault)
        plt.clf()
