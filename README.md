# dashboard_planting_weather
Dashboard for Planting and Weather
Overview:

Before startup, update the geocoordinates.txt file to your geocoordinates in the same format as the file.
How to get geocoordinates from gooogle:
Get the coordinates of a place
On your computer, open Google Maps.
Right-click the place or area on the map. This will open a pop-up window. You can find your latitude and longitude in decimal format at the top.
To copy the coordinates automatically, left click on the latitude and longitude.

You will need to have Python and PIP installed to run the program.
Required packages are located in requirements.txt, but the key items are the below:

streamlit
streamlit-autorefresh
pandas
requests
Pillow

Planting Database:
The planting schedules are based on the southeast US - you may need to update the data set prior to creating the database.
This list can be found in the plants_treatments_database.py file under the variable crops_list

For viewing/editing just the database itself
https://sqlitebrowser.org/dl/

Tracking fertilizer/chemical applications:
This is currently setup to accept tracking for neem oil, epsom salt, and fertilizer applications.
The tables store date only - these can be repurposed to track other applications.
If you want to update the button labels only, these are located on main_streamlit.py in the first container.
The functions to create the tables and update the database are located on main_streamlit.py.

Weather API:
This is setup to poll NOAA's weather API for hourly forecast every 60 minutes. 
Other sources can be used - the function under noaa_weather_api.py would need to be updated accordingly.

Weather Images:
Currently this is only set to include 2 images. One for if there is rain or storm in the current hour forecast text, and one for normal.
This can be expanded by expanding the if statements in the 2nd container in column 3 to include cases for more keywords.
the images can be replaced by stopping the streamlit application and replacing the files with a new file of the same name, or updating the file reference in the if statement.

Running Streamlit (Windows):
Open Command prompt
cd to the directory where the .py files are stored (Crops_Weather_Final is the folder)
type streamlit run main_streamlit.py
streamlit will autolaunch the application in your default browser. Local network access is possible by noting the network URL from the command prompt.
