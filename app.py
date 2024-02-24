import streamlit as st
import pandas as pd
import plotly.express as px

def home_page():
    st.title("World Happiness Visualization")
    st.text("This site will visualize data for you")
    st.image("h.jpg", caption="happy happy", use_column_width=True)

def stats(df):
    st.header("Statistics Summary")
    st.table(df.describe().style.set_properties(**{'max-height': '200px',
                                                 'max-width': '1000px',
                                                  'font-size': '15px'}))

def plot(df):
    st.header("Root Cause Visualization")
    type = st.selectbox("Select the type of Visualization", options=["Line Plot", "Choropleth Map"])

    if type == "Line Plot":
        country = st.selectbox("Select the Country", options=df['Country name'].unique())
        filter = df[df['Country name'] == country]
        factor = st.selectbox("Select the Factor", 
                          options=['Life Ladder and GDP', 
                                    'Life Expectancy',
                                    'Social Support, Freedom, Generosity & Corruption'])
    
        if factor == 'Life Ladder and GDP':
            fig2 = px.line(filter, x='year', y= ['Life Ladder', 'Log GDP per capita'], 
                color_discrete_sequence=px.colors.qualitative.Plotly,
                markers=True,
                title=f'{factor} of {country}')
            fig2.update_layout(plot_bgcolor='#AAEFED',
                       xaxis=dict(tickfont=dict(size=17)),
                       yaxis=dict(tickfont=dict(size=17)))
            st.plotly_chart(fig2)

        elif factor == 'Life Expectancy':
            fig2 = px.line(filter, x='year', y=['Healthy life expectancy at birth'], 
                color_discrete_sequence=['blue'],
                markers=True,
                title=f'{factor} of {country}')
            fig2.update_layout(plot_bgcolor='#AAEFED',
                       xaxis=dict(tickfont=dict(size=17)),
                       yaxis=dict(tickfont=dict(size=17)))
            st.plotly_chart(fig2)

        elif factor == 'Social Support, Freedom, Generosity & Corruption':
            fig2 = px.line(filter, x='year', y=['Social support', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'], 
                color_discrete_sequence=px.colors.qualitative.Plotly,
                markers=True,
                title=f'{factor} of {country}')
            fig2.update_layout(plot_bgcolor='#AAEFED',
                       xaxis=dict(tickfont=dict(size=17)),
                       yaxis=dict(tickfont=dict(size=17)))
            st.plotly_chart(fig2)
    
    
    elif type == "Choropleth Map":
        var = st.selectbox("Select the factor", options=['Life Ladder', 
                                                        'Log GDP per capita',
                                                        'Social support',
                                                        'Healthy life expectancy at birth',
                                                        'Freedom to make life choices',
                                                        'Generosity',
                                                        'Perceptions of corruption'])
        year = st.select_slider("Select the year", options=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
        filter = df[df['year'] == year]
        fig = px.choropleth(filter,
                    locations='Country name',
                    locationmode='country names',
                    color = var ,
                    hover_name='Country name',
                    scope="world",
                    width=800,
                    height=800,
                    color_continuous_scale='Plotly3')

        st.plotly_chart(fig)


def main():
    st.sidebar.title("Navigation")

    options = st.sidebar.radio("Pages", options=[
    "Home",
    "Statistics",
    "Root Cause Visualization"
    ])

    df = pd.read_csv("DataForTable2.1WHR2023.csv")
    df.drop(columns=['Positive affect', 'Negative affect'], inplace=True)

    if options == "Statistics":
        stats(df)
    elif options == "Home":
        home_page()
    elif options == "Root Cause Visualization":
        plot(df)
    


if __name__ == "__main__":
    main()