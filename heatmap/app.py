from flask import Flask, render_template, request
import pandas as pd
import requests
from io import StringIO
import plotly.express as px
import folium
from folium.plugins import HeatMap, MiniMap
from branca.colormap import LinearColormap

app = Flask(__name__)

# Main Route
@app.route('/', methods=['GET', 'POST'])
def home():
    incidentTypeOptions = ["All Incidents", "Roadside Assistance", "Colission", "Carjacking", "Total Loss"]
    townOptions = ["Mexico City", "Álvaro Obregón", "Azcapotzalco", "Benito Juárez", "Coyoacán", "Cuajimalpa de Morelos", "Cuahutémoc", "Gustavo A. Madero", "Iztacalco", "Iztapalapa", "Magdalena Contreras", "Miguel Hidalgo", "Milpa Alta", "Tláhuac", "Tlalpan", "Venustiano Carranza", "Xochimilco"]
    criteriaOptions = ["Ocurrences", "Total Cost"]

    if request.method == 'POST':
        Incident  = request.form.get('incidentType')
        Town = request.form.get('town')
        Criteria = request.form.get('criteria')

    else:
        Incident = "All Incidents"
        Town = "Mexico City"
        Criteria = "Total Cost"


        ### IMPORTING THE DATABASE

    # Function to download the file and handle exceptions
    def downloadFromGithub(url):
        response = requests.get(url)
        response.raise_for_status()
        return pd.read_csv(StringIO(response.text))

    # URL from CSV file on GitHub
    csv_url = "https://raw.githubusercontent.com/flavioAlvarezD/databases/CarInsurance/carInsurance.csv"
    # Downloads the CSV file and makes a dataframe out of it
    townList = downloadFromGithub(csv_url)


        ### REMAPPING THE INPUTS

    # Remaps Incident Value
    mappingsE = {
        "All Incidents": None,
        "Roadside Assistance": "Roadside Assistance",
        "Colission": "Colission",
        "Carjacking": "Carjacking",
        "Total Loss": "Total Loss"
    }

    def remapeo3(input):
        return mappingsE.get(input, "Error")
    incidentType = remapeo3(Incident)

    # Remaps Town Value
    mappingsD = {
        "Mexico City": None,
        "Álvaro Obregón": "alvaroObregon",
        "Azcapotzalco": "azcapotzalco",
        "Benito Juárez": "benitoJuarez",
        "Coyoacán": "coyoacan",
        "Cuajimalpa de Morelos": "cuajimalpa",
        "Cuahutémoc": "cuahutemoc",
        "Gustavo A. Madero": "gustavo",
        "Iztacalco": "iztacalco",
        "Iztapalapa": "iztapalapa",
        "Magdalena Contreras": "magdalena",
        "Miguel Hidalgo": "miguelHidalgo",
        "Milpa Alta": "milpaAlta",
        "Tláhuac": "tlahuac",
        "Tlalpan": "tlalpan",
        "Venustiano Carranza": "venustiano",
        "Xochimilco": "xochimilco"
    }

    def remapeo1(input):
        return mappingsD.get(input, "Error")
    town = remapeo1(Town)

    # Remaps Criteria Value
    mappingsC = {
        "Ocurrences": "incidentsByLoc",
        "Total Cost": 'costByLoc'
    }

    def remapeo2(input):
        return mappingsC.get(input, "Error")
    criteria = remapeo2(Criteria)


        ### BUG FIX, DATA CLEANSING AND FILTERING

    # Deletes Null values on lat and lon
    towns = townList.dropna(subset=['lon', 'lat'])
    # Bug Fix (considers "columns" as an Objet instead of a Float)
    towns = towns[(towns['lon'] != '#VALOR!') & (towns['lat'] != '#VALOR!')]
    towns[['lon', 'lat']] = towns[['lon', 'lat']].astype(float)
    # Creates "coord" column. So it generates an unique location for each row
    towns['coord'] = towns['lon'].astype(str) + '&' + towns['lat'].astype(str)
    # Counts incident ocurrences by each unique location
    towns['incidentsByLoc'] = towns.groupby('coord')['coord'].transform('count')
    # Sum the total incident cost by each location
    towns['costByLoc'] = towns.groupby('coord')['serviceCost'].transform('sum')
    # Drops location duplicates
    towns = towns.drop_duplicates(subset='coord')

    # Filters the dataframe by the selected incident
    if incidentType is not None:
        townsE = towns[towns['serviceType'] == incidentType]
    else:
        townsE = towns

    # Filters the dataframe by the selected town
    if town is not None:
        townsF = townsE[townsE['town'] == town]
    else:
        townsF = townsE


         ### HEATMAP CREATION

    # HeatMap's definition
    fig1 = px.density_mapbox(townsF, lat='lat', lon='lon', z=criteria, radius=30,
                            center=dict(lat=19.35421, lon=-99.06565), zoom=11.4,
                            mapbox_style="open-street-map", height=400)
    mapita = folium.Map(location=[19.35421, -99.06565], zoom_start=11.2, control_scale=True)

    mapValues = townsF[['lat', 'lon', criteria]]
    dataI = mapValues.values.tolist()
    hm = HeatMap(dataI, min_opacity=0.05, max_opacity=0.9, radius=25).add_to(mapita)

    #Generates a colored line useful to have a value reference
    colormap = LinearColormap(['blue', 'green', 'yellow', 'red'], caption=Criteria, vmin=mapValues[criteria].min(), vmax=mapValues[criteria].max())
    colormap.add_to(mapita)

    #Puts a title on the heatmap
    title_html = f'<div style="background-color: #cfe2f3; padding: 11px; border-radius: 5px; text-align: center;"><h3 style="font-size:26px; color:#073763; margin: 0;"><b>HeatMap of {Incident} in {Town} by {Criteria}</b></h3></div>'
    mapita.get_root().html.add_child(folium.Element(title_html))

    #Generates a minimap to see where in the country is the heatmap located
    minimap = MiniMap(position='bottomleft', width=120, height=110, zoom_animation=True, auto_toggle=True).add_to(mapita)

    return render_template('index.html', folium_map=mapita._repr_html_(), townOptions=townOptions, criteriaOptions=criteriaOptions, incidentTypeOptions=incidentTypeOptions)

if __name__ == '__main__':
    app.run(debug=True)