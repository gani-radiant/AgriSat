import pandas as pd
import folium

data=pd.read_excel("collegeBtech.xlsx")
data.head()
fg=folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(data=(open("ts_districts.json","r",encoding="utf-8-sig").read())))
#location = data['Latitude'].mean(), data['Longitude'].mean()
map = folium.Map(location=[20.0000,75.0000],zoom_start=10)
for i in range(0,len(data)):  
    #labels=data['College name'].iloc[i]
    #folium.Marker([data['Latitude'].iloc[i],data['Longitude'].iloc[i]],popup=labels,
                # icon=folium.Icon(icon='university', prefix='fa',color='pink')).add_to(map)
    def popup_html(row):
        i=row
        college_name=data["Locations"].iloc[i]
        courses=data["Crops"].iloc[i]
        rating=data["Paddy"].iloc[i]
        cutoff=data["Pulses"].iloc[i]
        place=data["Sugarcane"].iloc[i]
        image=data["Image"].iloc[i]
        left_col_color = "#3e95b5"
        right_col_color = "#f2f9ff"
        html="""
    <!DOCTYPE html>
    <html>
    <center><img src=\"""" + image + """\"  width=500 height=200 ></center>
    <center><h4 style="margin-bottom:5"; width="200px">{}</h4>""".format(college_name) + """</center>
    <center> <table style="height: 126px; width: 305px;">
    <tbody>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;"><h4>Courses available: </h4></span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(courses) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Rating: </span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(rating) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">CutOff rank: </span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(cutoff) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Address: </span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(place) + """
    </tr>
    </tbody>
    </table></center>
    </html>
    """
        return html
    html=popup_html(i)
    popup=folium.Popup(folium.Html(html,script=True),max_width=500)
    folium.Marker([data['Latitude'].iloc[i],data['Longitude'].iloc[i]],popup=popup,icon=folium.Icon(color='green',icon='location',prefix='fa')).add_to(map)
map
map.add_child(fg)
map.save("ts.html")