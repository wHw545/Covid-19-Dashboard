# import bar_chart_race as bcr
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import plotly.express as px
import numpy as np
import datetime
# import plotly.graph_objects as go
# from raceplotly.plots import barplot
#from ipywidgets import interact, interactive, fixed, interact_manual
#import dash_core_components as dcc
#import ipywidgets as widgets

def main():
    
    
    st.markdown("<h1 style='font-size: 24pt;text-align: center;'><strong><u>Covid-19 Dashboard</u></strong></h1>", unsafe_allow_html=True)
    
  
    st.sidebar.markdown("<h1 style='font-size: 24pt;text-align: center;'><strong><u>Covid-19 Dashboard</u></strong></h1>", unsafe_allow_html=True)
    
    st.markdown("This Dashboard is a resource to help advance the understanding of the virus, inform the public, and brief policymakers in order to guide a response, improve care, and save lives.", unsafe_allow_html=True)
    
    death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')
    
    # print(recovered_df)
    # print(confirmed_df)
    
    
    
    country_df.columns = map(str.lower, country_df.columns)
    death_df.columns = map(str.lower, death_df.columns)
    confirmed_df.columns = map(str.lower, confirmed_df.columns)
    recovered_df.columns = map(str.lower, recovered_df.columns)
    
    confirmed_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    recovered_df = recovered_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    death_df = death_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    country_df = country_df.rename(columns={'country_region': 'country'})
    
    
    # drop_confirmed_NaN_df = confirmed_df.dropna(subset=['lat','long'])
    # world_map_confirmed = folium.Map(location=[11,0], tiles="cartodbpositron", zoom_start=1, max_zoom = 6, min_zoom = 0)

    


#bar chart time series for confirmed
    bar_chart_country = confirmed_df.drop(columns=['lat','long','state'])
    bar_chart_country6 = bar_chart_country.set_index(['country'])
    bar_chart_country2 = bar_chart_country6.transpose()
    bar_chart_country3 = bar_chart_country2.reset_index()
    bar_chart_country4 = bar_chart_country3.rename(columns={'index':'Date'})
    bar_chart_country5 = bar_chart_country4.set_index('Date')
    line_chart_country = bar_chart_country5.reset_index()
    line_chart_country[['Date']] = line_chart_country[['Date']].apply(pd.to_datetime)
    line_chart_country2 = line_chart_country.set_index('Date')
    # line_chart_country2 = pd.to_datetime(line_chart_country['Date'])
    # line_chart_country2 = bar_chart_country5['Date'].apply(pd.to_datetime)
    
    
    
    
    
    
    
   
#bar chart time series for recovered
    bar_chart_recovered = recovered_df.drop(columns=['lat','long','state'])
    bar_chart_recovered6 = bar_chart_recovered.set_index(['country'])
    bar_chart_recovered2 = bar_chart_recovered6.transpose()
    bar_chart_recovered3 = bar_chart_recovered2.reset_index()
    bar_chart_recovered5 = bar_chart_recovered3.rename(columns={'index':'Date'})
    bar_chart_recovered4 = bar_chart_recovered5.set_index('Date')
    line_chart_recovered = bar_chart_recovered4.reset_index()
    line_chart_recovered[['Date']] = line_chart_recovered[['Date']].apply(pd.to_datetime)
    line_chart_recovered2 = line_chart_recovered.set_index('Date')
    
#bar chart time series for death
    bar_chart_deaths = death_df.drop(columns=['lat','long','state'])
    bar_chart_deaths6 = bar_chart_deaths.set_index(['country'])
    bar_chart_deaths2 = bar_chart_deaths6.transpose()
    bar_chart_deaths3 = bar_chart_deaths2.reset_index()
    bar_chart_deaths5 = bar_chart_deaths3.rename(columns={'index':'Date'})
    bar_chart_deaths4 = bar_chart_deaths5.set_index('Date')
    line_chart_deaths = bar_chart_deaths4.reset_index()
    line_chart_deaths[['Date']] = line_chart_deaths[['Date']].apply(pd.to_datetime)
    line_chart_deaths2 = line_chart_deaths.set_index('Date')
    
# #for bar chart race
           
#     sorted_death_df1 = sorted_death_df.drop(columns=['lat', 'long','state'])

#     sorted_death_df2 = sorted_death_df1.set_index(['country'])
#     sorted_death_df3 = sorted_death_df2.transpose()

#     sorted_death_df4 = sorted_death_df3.reset_index()
#     sorted_death_df5 = sorted_death_df4.rename(columns={'index':'Date'})
#     sorted_death_df9 = sorted_death_df5.set_index('Date')
#     sorted_death_df6 = sorted_death_df9.head(5)
    
    drop_confirmed_NaN_df = confirmed_df.dropna(subset=['lat','long'])
    
    
    
    world_map_confirmed = folium.Map(location=[11,0], tiles="cartodbpositron", zoom_start=1, max_zoom = 6, min_zoom = 0)

    for i in range(0,len(drop_confirmed_NaN_df)):
        folium.Circle(
            location=[drop_confirmed_NaN_df.iloc[i]['lat'], drop_confirmed_NaN_df.iloc[i]['long']],
            fill=True,
            radius=(int((np.log(drop_confirmed_NaN_df.iloc[i,-1]+1.00001)))+0.2)*50000,
            color='red',
            fill_color='indigo',
            tooltip = "<div style='margin: 0; background-color: black; color: white;'>"+
                    "<h4 style='text-align:center;font-weight: bold'>"+drop_confirmed_NaN_df.iloc[i]['country'] + "</h4>"
                    "<hr style='margin:10px;color: white;'>"+
                    "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                        "<li>Confirmed: "+str(drop_confirmed_NaN_df.iloc[i,-1])+"</li>"+
                        "<li>Deaths:   "+str(death_df.iloc[i+1,-1])+"</li>"+ #1056
                        "<li>Death Rate: "+ str(np.round(death_df.iloc[i+1,-1]/(drop_confirmed_NaN_df.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                    "</ul></div>",
        ).add_to(world_map_confirmed)
    
    
    
    
    world_map_recovered = folium.Map(location=[11,0], tiles="cartodbpositron", zoom_start=1, max_zoom = 6, min_zoom = 0)


    for i in range(0,len(drop_confirmed_NaN_df)):
        folium.Circle(
            location=[drop_confirmed_NaN_df.iloc[i]['lat'], drop_confirmed_NaN_df.iloc[i]['long']],
            fill=True,
            radius=(int((np.log(drop_confirmed_NaN_df.iloc[i,-1]+1.00001)))+0.2)*50000,
            color='red',
            fill_color='indigo',
            tooltip = "<div style='margin: 0; background-color: black; color: white;'>"+
                    "<h4 style='text-align:center;font-weight: bold'>"+drop_confirmed_NaN_df.iloc[i]['country'] + "</h4>"
                    "<hr style='margin:10px;color: white;'>"+
                    "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                        "<li>Confirmed: "+str(drop_confirmed_NaN_df.iloc[i,-1])+"</li>"+
                        "<li>Recovered:   "+str(recovered_df.iloc[i-14,-1])+"</li>"+ #280707
                        "<li>Recovered Rate: "+ str(np.round(recovered_df.iloc[i-14,-1]/(drop_confirmed_NaN_df.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                    "</ul></div>",
        ).add_to(world_map_recovered)
    
    
   
    world_map_death = folium.Map(location=[11,0], tiles="cartodbpositron", zoom_start=1, max_zoom = 6, min_zoom = 0)


    for i in range(0,len(drop_confirmed_NaN_df)):
        folium.Circle(
            location=[drop_confirmed_NaN_df.iloc[i]['lat'], drop_confirmed_NaN_df.iloc[i]['long']],
            fill=True,
            radius=(int((np.log(drop_confirmed_NaN_df.iloc[i,-1]+1.00001)))+0.2)*50000,
            color='red',
            fill_color='indigo',
            tooltip = "<div style='margin: 0; background-color: black; color: white;'>"+
                    "<h4 style='text-align:center;font-weight: bold'>"+drop_confirmed_NaN_df.iloc[i]['country'] + "</h4>"
                    "<hr style='margin:10px;color: white;'>"+
                    "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                        #"<li>Confirmed: "+str(drop_confirmed_NaN_df.iloc[i,-1])+"</li>"+
                        "<li>Deaths:   "+str(death_df.iloc[i,-1])+"</li>"+
                        #"<li>Death Rate: "+ str(np.round(death_df.iloc[i,-1]/(drop_confirmed_NaN_df.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                    "</ul></div>",
        
        ).add_to(world_map_death)
        #world_map_death.add_child(HeatMap(zip('lat','long','deaths'),radius=0))
        
     
        
        
        
        
    covid1 = country_df.drop(columns=['last_update','lat','long_','incident_rate','people_tested','people_hospitalized','mortality_rate','uid','iso3'],axis=1) 
    
    covid_confirmed = covid1.sort_values('confirmed', ascending= False).head(20)
    covid_recovered = covid1.sort_values('recovered', ascending= False).head(20)
    covid_active = covid1.sort_values('active', ascending= False).head(20)
    covid_deaths = covid1.sort_values('deaths', ascending= False).head(20)
    
    
    
    total_confirmed = covid1['confirmed'].sum()
    st.write('TOTAL CONFIRMED CASES FROM ALL OVER THE WORLD - ',total_confirmed)
    total_recovered = covid1['recovered'].sum()
    st.write('TOTAL RECOVERED CASES FROM ALL OVER THE WORLD - ',total_recovered)
    total_deaths = covid1['deaths'].sum()
    st.write('TOTAL DEATHS CASES FROM ALL OVER THE WORLD - ',total_deaths)
    total_active = covid1['active'].sum()
    st.write('TOTAL ACTIVE CASES FROM ALL OVER THE WORLD - ',total_active)
    
    
    st.sidebar.subheader('Map Analysis')
    
    select = st.sidebar.selectbox('Choose Map Type',['Confirmed Cases','Recovered Cases','Deaths Cases'],key='1')
    
    
    if not st.sidebar.checkbox("Hide Map",True):
        
        if select == "Confirmed Cases": 
           st.subheader("Total Confirmed Case - World")
           folium_static(world_map_confirmed)
           
           
           
        elif select == "Recovered Cases":
           st.subheader("Total Recovery Case - World")
           folium_static(world_map_recovered)
          
           
           
        else:
           st.subheader("Total Deaths Case - World")
           folium_static(world_map_death)
    
    
    
    
    
    # st.subheader("Covid-19 Top 20 Worst Hit Data")
     


    select_country = st.selectbox("Select Country",covid1["country"][:186])
    st.header(f"Latest Summary of Covid-19 infections for {select_country}")
    
    total_confirmed_per_country = covid1[covid1["country"]==select_country]['confirmed'].sum()

    total_recovered_per_country = covid1[covid1["country"]==select_country]['recovered'].sum()
    
    total_active_per_country = covid1[covid1["country"]==select_country]['active'].sum()

    total_deaths_per_country = covid1[covid1["country"]==select_country]['deaths'].sum()
    
    show = {"Category":["Total Confirmed Cases","Total Recovered Cases","Total Deaths Cases","Total Active Cases"],
       "Total":[total_confirmed_per_country, total_recovered_per_country,total_deaths_per_country,total_active_per_country]}
    stat = pd.DataFrame(show)
    st.table(stat)

    
   
    
    
    
    
       
    #bar chart 
    st.sidebar.subheader('Bar Chart Analysis')
    select = st.sidebar.selectbox('Choose Bar Type',['Confirmed Cases','Recovered Cases','Deaths','Active Cases'],key='2')
    if not st.sidebar.checkbox("Hide Bar Chart",True):
        
        if select == "Confirmed Cases": 
            select_country2 = select_country
           
            st.header(f"Summary of Confirmed Cases Over Time {select_country2}")
            fig2 = px.bar(bar_chart_country5, x=bar_chart_country5.index, y=select_country2)
            st.plotly_chart(fig2) 

            fig = px.bar(covid_confirmed.head(20), y='confirmed',x='country',color='country',height=400)
            fig.update_layout(title='Comparison of Total Confirmed Cases of 20 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Confirmed Case',template="seaborn")
            st.plotly_chart(fig)

           #labels=dict(x="Fruit", y="Amount", color="Place")
                 
        elif select == "Recovered Cases":
           
           select_country2 = select_country
           
           st.header(f"Summary of Recovered Cases Over Time {select_country2}")
           fig2 = px.bar(bar_chart_recovered4, x=bar_chart_recovered4.index, y=select_country2)
           st.plotly_chart(fig2) 
            
           fig = px.bar(covid_recovered.head(20), y='recovered',x='country',color='country',height=400)
           fig.update_layout(title='Comparison of Total Recovered of 20 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Recovered',template="seaborn")
           st.plotly_chart(fig)
            
        elif select == "Deaths":
           select_country2 = select_country
           
           st.header(f"Summary of Deaths Cases Over Time {select_country2}")
           fig2 = px.bar(bar_chart_deaths4, x=bar_chart_deaths4.index, y=select_country2)
           st.plotly_chart(fig2) 
            
           fig = px.bar(covid_deaths.head(20), y='deaths',x='country',color='country',height=400)
           fig.update_layout(title='Comparison of Total Deaths of 20 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Deaths',template="seaborn")
           st.plotly_chart(fig) 
           
        else:
    
           fig = px.bar(covid_active.head(20), y='active',x='country',color='country',height=400)
           fig.update_layout(title='Comparison of Active Cases of 20 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Active',template="seaborn")
           st.plotly_chart(fig)
           
                   
          
          
    
    
    st.sidebar.subheader('Line Chart Analysis')
    select = st.sidebar.selectbox('Choose Line Type',['Confirmed Cases','Recovered Cases','Deaths'],key='3')
    
    if not st.sidebar.checkbox("Hide Line Chart",True):
        
        if select == "Confirmed Cases": 
            
            today = datetime.datetime.strptime("2020-01-22","%Y-%m-%d")
            tomorrow =  datetime.datetime.strptime("2021-04-12","%Y-%m-%d")
            
            start_date = st.date_input('Start date - starting date', today)
            end_date = st.date_input('End date', tomorrow)
            if start_date < end_date:
                st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
            else:
                st.error('Error: End date must fall after start date.')
            
            select_country3 = select_country
            
            
            # tru_range = (line_chart_country2 >= today) & (line_chart_country2 <= tomorrow)
            # # print(line_chart_country3.loc[tru_range])
            # line_chart_country3 = line_chart_country.loc[tru_range]
            
            
            fig_confirmed = px.line(line_chart_country2, x=line_chart_country2.index, y=select_country3,title='Confirmed Cases Line Chart')
            # fig_confirmed = px.line(line_chart_country, x=line_chart_country4, y=select_country3, title='Confirmed Cases Line Chart')
    
            fig_confirmed.update_xaxes(
                rangeslider_visible=True
            )
                                     
            fig_confirmed.update_layout(
                xaxis_title="Date",
                xaxis_range=[start_date,end_date])
            
            st.plotly_chart(fig_confirmed)
            # #fig_confirmed.show()
            
            
            
            
        
            
        elif select == "Recovered Cases":
            
            today = datetime.datetime.strptime("2020-01-22","%Y-%m-%d")
            tomorrow =  datetime.datetime.strptime("2021-04-12","%Y-%m-%d")
            
            start_date = st.date_input('Start date - starting date', today)
            end_date = st.date_input('End date', tomorrow)
            if start_date < end_date:
                st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
            else:
                st.error('Error: End date must fall after start date.')
            
            select_country4 = select_country
            
            fig_recovered = px.line(line_chart_recovered2, x=line_chart_recovered2.index, y=select_country4, title='Recovered Cases Line Chart')
            
            
            
            fig_recovered.update_xaxes(
                rangeslider_visible=True
            )
                                     
            fig_recovered.update_layout(
                xaxis_title="Date",
                xaxis_range=[start_date,end_date])
            st.plotly_chart(fig_recovered)
            
        else: 
           
            today = datetime.datetime.strptime("2020-01-22","%Y-%m-%d")
            tomorrow =  datetime.datetime.strptime("2021-04-12","%Y-%m-%d")
            
            start_date = st.date_input('Start date - starting date', today)
            end_date = st.date_input('End date', tomorrow)
            if start_date < end_date:
                st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
            else:
                st.error('Error: End date must fall after start date.')
           
            
           
            select_country5 = select_country  
            fig_deaths = px.line(line_chart_deaths2, x=line_chart_deaths2.index, y=select_country5, title='Deaths Cases Line Chart')
           
            fig_deaths.update_xaxes(
                rangeslider_visible=True
            )
                                     
            fig_deaths.update_layout(
                xaxis_title="Date",
                xaxis_range=[start_date,end_date])
           
            st.plotly_chart(fig_deaths)
        
        
    
        
      

        
       
        
        
        
    #   #bar chart race
    # st.sidebar.subheader(' Bar Chart Race Analysis ')
    
    # select = st.sidebar.selectbox('Choose Bar Chart',['Confirmed Cases','Recovered Cases','Active Cases','Deaths'],key='4')
    
           
           
    # if not st.sidebar.checkbox("Hide Bar Chart Race",True):
        
    #     if select == "Confirmed Cases": 
            
            
    #         my_raceplot = barplot(line_chart_country2,
    #                   item_column=line_chart_country2.columns,
    #                   value_column=line_chart_country2.values,
    #                   time_column=line_chart_country2.iloc[:,0])

    #         my_raceplot.plot(item_label = 'Top 10 crops', value_label = 'Production quantity (tonnes)', frame_duration = 800)
                             
            
           
           
    #     elif select == "Recovered Cases":
            
    #        fig = px.bar(covid_recovered.head(10), y='recovered',x='country',color='country',height=400)
    #        fig.update_layout(title='Comparison of Total Recovered of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Recovered',template="plotly_dark")
    #        st.plotly_chart(fig)
            
           
    #     elif select == "Active Cases":
            
    #        fig = px.bar(covid_active.head(10), y='active',x='country',color='country',height=400)
    #        fig.update_layout(title='Comparison of Active Cases of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Recovered',template="plotly_dark")
    #        st.plotly_chart(fig)
            
           
    #     else:
    #       bcr.bar_chart_race(df = sorted_death_df6, title = "death daily ")
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    main()
    
    st.markdown("@Covid-19 Dashboard")
