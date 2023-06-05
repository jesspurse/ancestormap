# Imports packages
    # Mapping tool
import cartopy.crs as ccrs
import cartopy
import cartopy.io.img_tiles as cimgt

    # Plotting tool
import matplotlib.pyplot as plt
import matplotlib

    # Data tools
import csv
import pandas as pd

# Imports data
    # because the files you created in SAS don't have column names
    # it's imperative that you make sure they are named correctly here
for i in range(200912,200913):
    df = pd.read_csv(r'path/ancestors_%d.csv' % i,
                 names=["gender","year","lat","lon"])

    stamen_terrain = cimgt.Stamen('terrain-background')
    matplotlib.use('agg')
    plt.ioff()

# Makes plot and axes
    fig=plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree()) #female

# Adds background
    ax.add_image(stamen_terrain, 8)

# Adds different features to map
    ax.coastlines(linewidth=1.7)
    ax.add_feature(cartopy.feature.RIVERS, edgecolor='black', linewidth=1.3)
    ax.add_feature(cartopy.feature.LAKES, edgecolor='black', linewidth=1.3)
    ax.add_feature(cartopy.feature.BORDERS, linewidth=2.7)

# Adds borders
    ax.spines['geo'].set_edgecolor('black')
    ax.spines['geo'].set_linewidth(6)

# Sets figure size
    fig.set_size_inches(37, 16)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Sets the lat/long of the map frame

    # This allows changing the focus after a certain date
    # It's [W, E, S, N]
    # The text location needs to be changed also.

#406 - 454
#    ax.set_extent([-12, 50, 30, 59], crs=ccrs.PlateCarree())
 #   date_x= 46
  #  date_y= 30.2

#580 - 830
#    ax.set_extent([-12, 50, 30, 59], crs=ccrs.PlateCarree())
 #   date_x= 46
  #  date_y= 30.2

#830 - 1000
#    ax.set_extent([-12, 50, 30, 66], crs=ccrs.PlateCarree())
 #   date_x= 45
  #  date_y= 30.2

#1000 - 1084
#    ax.set_extent([-12, 50, 30, 66], crs=ccrs.PlateCarree())
 #   date_x= 43.8
  #  date_y= 30.2

#1084 - 1275
#    ax.set_extent([-12, 50, 30, 59], crs=ccrs.PlateCarree())
 #   date_x= 45
  #  date_y= 30.2

#1275 - 1591
#    ax.set_extent([-12, 10, 42, 59], crs=ccrs.PlateCarree())
 #   date_x= 7
  #  date_y= 42.2

#1591 - 1750
#    ax.set_extent([-90, -40, 25, 59], crs=ccrs.PlateCarree())
 #   date_x= -46
  #  date_y= 25.2

#1750 - 1878
#    ax.set_extent([-102, 1, 33, 59], crs=ccrs.PlateCarree())            
 #   date_x= -6.8
  #  date_y= 33.3

#1878 - 1920
#    ax.set_extent([-140, 26, 35, 59], crs=ccrs.PlateCarree())            
 #   date_x= 12
  #  date_y= 35.2

#1920 - 1950
#    ax.set_extent([-140, -30, 35, 59], crs=ccrs.PlateCarree())            
 #   date_x= -39
  #  date_y= 35.2

#1950 - 1973:
#    ax.set_extent([-128, -53, 35, 52], crs=ccrs.PlateCarree())
 #   date_x= -58.5
  #  date_y= 35.2

#1973 - 2023
    ax.set_extent([-126, -66, 24, 50], crs=ccrs.PlateCarree())
    date_x= -70.5
    date_y= 24.2

# Plots each dot
    #the color depends on the gender, you can add other genders

    colors = {'M':'blue','F':'red'}
    ax.scatter(df['lon'],df['lat'],marker='o', s=400,c=df['gender'].map(colors))

# Adds the text to show the year
    ax.text(date_x, date_y,"%d" % i,color='black',
            fontname='Sans Serif', fontsize=78,transform=ccrs.PlateCarree())

# Saves the map
    fig.savefig(f"path/frame_%d.png" % i, dpi=175,transparent=True,facecolor='black')
    plt.close(fig)

# Print years that was just created (this is useful so you know where you are)

    # I also had some images where there was an internet lag
    # and some of the map background didn't print so I needed to re-run them

    print("%d" % i)
