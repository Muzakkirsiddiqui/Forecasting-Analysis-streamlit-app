import matplotlib.pyplot as plt
import streamlit
import streamlit as st
import pandas as pd
import matplotlib as pyplot
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objs as go



st.markdown(""" <style> .font {
font-size:80px ; font-family: 'Cooper Black'} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">FORECAST ANALYSIS 📈</p>', unsafe_allow_html=True)


#File upload
uploaded_file=st.file_uploader('Upload Files',type=['csv'])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)

    if st.checkbox("SHOW ENTIRE DATA"):
        st.dataframe(df)



    # Selecter
    option = st.sidebar.selectbox(
    'PRODUCT_NAME',
    df['PROD_NAME'].unique())

    option_Y = st.sidebar.selectbox(
    'YEAR',
    df['YEAR'].unique())

    option_M = st.sidebar.selectbox(
    'MONTH',
    df['MONTH'].unique())


    option_Select=st.sidebar.selectbox("Select",options=('QUANTITY BY PRODUCT AT EACH YEAR','QUANTITY W.R.T SELECTED MONTH'))



    st.dataframe(
        df.loc[(df['PROD_NAME'] == option) & (df['YEAR'] == int(option_Y)) & (df['MONTH'] == int(option_M))])
    if option_Select=="QUANTITY BY PRODUCT AT EACH YEAR":
        st.markdown(""" <style> .font {
               font-size:20px ; font-family: 'Cooper Black'} 
               </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">QUANTITY BY PRODUCT AT EACH YEAR</p>', unsafe_allow_html=True)

        # MONTHLY QUANTITY AT SELECTED YEAR
        MApe = df.loc[(df['PROD_NAME'] == option) & (df['YEAR'] == int(option_Y)) & (df['MONTH'] == int(option_M))][
            'APE']
        try:
            st.write(f"THE MAPE WIll BE ", MApe.values[0], '%', ':rocket:', 'IN', option_Y,'📈' ,option)
        except:
            st.write("NO Value Found")

        DF_1 = df.loc[(df['YEAR'] == int(option_Y))]
        plot = DF_1.groupby(['MONTH']).sum(['ACTUAL_QUANTITY']).drop(['YEAR', 'APE'], axis=1)
        fig_1 = px.line(plot)
        st.write(fig_1)

    if option_Select=="QUANTITY W.R.T SELECTED MONTH":
        # QUANTITY W.R.T TO SELECTED MONTH
        MApe = df.loc[(df['PROD_NAME'] == option) & (df['YEAR'] == int(option_Y)) & (df['MONTH'] == int(option_M))][
            'APE']
        try:
            st.write(f"THE MAPE WIll BE ", MApe.values[0], '%', ':rocket:', 'IN', option_Y,'📈' ,option)
        except:
            st.write("NO Value Found")
        st.markdown(""" <style> .font {
                font-size:20px ; font-family: 'Cooper Black'} 
                </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">QUANTITY (W.R.T) SELECTED MONTH</p>', unsafe_allow_html=True)
        DF_1 = df.loc[(df['MONTH'] == int(option_M))]
        plot = DF_1.groupby(['YEAR']).sum(['ACTUAL_QUANTITY']).drop(['MONTH', 'APE'], axis=1)
        fig_1 = px.line(plot)
        st.write(fig_1)






    #Horizantal_Bar_plot
    st.markdown(""" <style> .font {
                   font-size:30px ; font-family: 'Cooper Black'} 
                   </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">MONTHLY SALES</p>', unsafe_allow_html=True)


    if st.checkbox("MONTHLY SALES BY PROD_NAME"):
        prodsales = df.groupby(['PROD_NAME', 'MONTH'])['ACTUAL_QUANTITY'].sum().reset_index()
        fig = px.bar(prodsales, x='ACTUAL_QUANTITY', y='PROD_NAME', orientation='h', height=600,color='PROD_NAME',
                     title='MONTHLY SALES BY PRODUCT ',
                     animation_frame="MONTH", animation_group="PROD_NAME", range_x=[0, 20000], template="seaborn")
        p = fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
        st.write(fig)



    # Pie Plot
    st.markdown(""" <style> .font {
                       font-size:30px ; font-family: 'Cooper Black'} 
                       </style> """, unsafe_allow_html=True)
    st.markdown('<p ACTUAL_QUANTITY BY PROD_NAME</p>', unsafe_allow_html=True)

    if st.checkbox("ACTUAL_QUANTITY BY PROD_NAME"):
        Makesales = df.groupby(['PROD_NAME'])['ACTUAL_QUANTITY'].sum().reset_index().sort_values(by='ACTUAL_QUANTITY')
        Makesales.loc[Makesales['ACTUAL_QUANTITY'] < 2.e4, 'PROD_NAME'] = 'Other PROD_NAME'  # Represent only large countries
        fig = px.pie(Makesales, values='ACTUAL_QUANTITY', names='PROD_NAME', template='seaborn')
        fig.update_layout(title_text='ACTUAL_QUANTITY BY PROD_NAME', title_x=0.45)
        st.write(fig)



