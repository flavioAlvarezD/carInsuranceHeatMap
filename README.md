                         _.:::CAR INSURANCE HEATMAP:::._

        1.- ABOUT THIS PROJECT
To be brief; this heatmap shows the ocurrences on sinister claims for an insurance company, along with their costs.

It uses flask as framework, pandas for an easy data work and plotly in conjuction with folium to build the heatmap.
The info is imported via a GitHub repository. If you'd like to see other ways to import data. Feel free to check my GitHub.
The index.html file contains the <style> CSS inside of it. And also the app.py archive has all the functions inside of it too.
Since this files are really short and no private tokens ares used, I didn't considered necessary to build separated files for this.

Now lets have some context:
Mexico city is divided on 16 different areas called "alcaldías".
Which are just like big neighborhoods but without a clear physical division.
I don't know and couldn't find an English word for this term, so I'll just call them "Towns"

What's the practical use for this?
The practical use for the Heatmap is to make decision making, easier.
Since managers can use it to comprehend in an easy and quick way which zones on the city are the most prone to have incidents, 
what kind of incidents and how much money they ended up costing for the company.

Managers could, as an example, rise the price of the insurance for people that lives near those areas, 
so the company can recover some money on the elevated insurance claims rate.
Or the oppossite; the company could decide to lower the prices to their clients that lives on the low risk areas.
And as you can figure, lower costs comes with more client interest on the service.

Granted; this is about car insurance, so is not expected for the people to stay home and not drive far from their houses.
However, a good amount of car accidents tend to happen really close to home, 
because of the false security feeling peole experiment when being near their houses.

Also this use depends on the kind of data you ingest into the app.
It could show the sales for an Ecommerce, crime rate, political supporters, market study, etc.
The best way I can summarize the usefulness of this heatmap would be "Decision Making"



        2.- INSTALL AND RUN

You just need to have python3 installed on your device.
>I recommend to create a virtual environment before installing any library
    python -m venv heatmap

    -Then you can activate the environment using the command
        heatmap\Scripts\activate (for Windows) OR source heatmap/bin/activate (for MacOs)

    -I also advice you to make sure you're not on the global environment by writing
        pip list

>If the list contains little to no libraries, then you're good to go. Install the libraries
    pip install flask pandas requests plotly folium branca

>Once installed, you can run the program by writing on your terminal
    pyton app.py

>Launch your web browser and enter the ip adress the terminal gave you



        3.- HOW TO USE THE HEATMAP
It's pretty straightforward; you just have to choose the incident type you wanna check on, 
the part of the city that interests you and the criteria you wish the "heat" to be based on.
If you chose "ocurrences" then the map will be colored by the number of times that incident has happened in that specific zone in the city.
If you select "Total Cost" then it will show how much money the company has spend on that kind of incident.

You can take the color line on the upper right side of the map as a reference. So you are aware of "how much" certain color means
And also see how the numbers change according to your election.



        4.- ROOM FOR IMPROVEMENT
This, more than an improvement is an alternative. As I said before, this app could support data from other industries and from different sources.
So yeah, you could use API's to call data on real time, pull data from a cloud database, or even use Web Scraping to build your dataset.
OBVIOUSLY you'll have to change the input and the column names. But that's an easy task.

Also the colorline bar could be placed outside the map, so it doesn't merge with the map colors. I'll make that change sometime in the future...



        5.- ABOUT ME
Hey there! Flavio Álvarez here. I'm a Data Scientist currently living in Mexico, with a good mileage and knowledge about Ecommerce.
I like videogames (as almost every other programmer, how unique), motorcycles, and I really love listening to 2000's rock.
You cand reach me on these links:
https://github.com/flavioAlvarezD
https://www.linkedin.com/in/flavio-alvarez-dorantes/

And thank you for reading this :D
