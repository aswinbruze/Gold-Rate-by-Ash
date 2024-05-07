import streamlit as st
from streamlit_option_menu import option_menu
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from req_gold import last_10days_data
import matplotlib.pyplot as plt
import plotly.express as px
#from st_lottie import st_lottie

##________________________________________________________________________________________________________________



##_________________________________________________________________________________________________________________

st.set_page_config("Gold Details",page_icon=":moneybag:")  # to set icon symbol
st.header("GOLD RATE BY ASH")

metric1_value = last_10days_data.iloc[0,3]
#metric2_value = last_10days_data.iloc[1,3]
  

    # Define delta values
delta1 =int(last_10days_data.iloc[0,5])
#delta2 = int(last_10days_data.iloc[1,5])
    


##_____________________________________________________________________________________________________________

st.image(r"goldimg3.jpg", caption=" GOLD IS GOLD! ", use_column_width=True)  # to display image

#"C:\Users\aswin.anbu.mani\Documents\goldimgbgrnd.jpg"
#"C:\Users\aswin.anbu.mani\Downloads\goldimg3.jpg"

##_______________________________________________________________________________________________________________
## Adding two columns  left side content right side image


# Set up a two-column layout
cols1, cols2 = st.columns([3, 1])

# Add content to the first column (left)
with cols1:
    st.markdown("Gold is the most useful metal in the world, with many special properties and applications. In this page you will get to know gold rate, graphical representation, sugestion and statistical details for last 10 days in CHENNAI/TAMIL NADU. It will be very useful to buy and analyse the gold data")
# Add content to the second column (right)
with cols2:
    st.image(r"IMG_20240426_164056.jpg", width= 150)



#st.subheader("Gold details today")
st.markdown("                                                                       ")
st.markdown("                                                                       ")
st.markdown("_________________________________________________________________________________")
st.markdown("                                                                       ")

##______________________________________________________________________________________________________
## left side menu bar setup

with st.sidebar:
    s = option_menu(
        menu_title = "Main menu",
        options = ["History Data","Graphical Representation","Buying Suggestion","Feedback"],
        #orientation= "horizontal",
    )
    
    
if s == "History Data":
    button1 = st.checkbox("Click here to view data")
    if button1:
        #Gold_data = pd.read_csv(r"C:\Users\aswin.anbu.mani\Downloads\nyctaxi\nyctaxi\green\last_10days_gold_data.csv")
        st.dataframe(last_10days_data)

else:
    pass
    #st.write("Select an option from the sidebar")
    #print(last_10days_data)
    
    
##_________________________________________________________________________________________________________

if s == "Buying Suggestion":
    col1, col2, col3,col4,col5 = st.columns(5)
    
    
    # Define metric values
    metric1_value = last_10days_data.iloc[0,3]
    metric2_value = last_10days_data.iloc[1,3]
    metric3_value = last_10days_data.iloc[2,3]
    metric4_value = last_10days_data.iloc[3,3]
    metric5_value = last_10days_data.iloc[4,3]

    # Define delta values
    delta1 =int(last_10days_data.iloc[0,5])
    delta2 = int(last_10days_data.iloc[1,5])
    delta3 = int(last_10days_data.iloc[2,5])
    delta4 = int(last_10days_data.iloc[3,5])
    delta5 = int(last_10days_data.iloc[4,5])

    # Display metrics in each column
    with col1:
        st.metric(last_10days_data.iloc[0,0], metric1_value, delta=delta1, delta_color="inverse")

    with col2:
        st.metric(last_10days_data.iloc[1,0], metric2_value, delta2,delta_color="inverse")

    with col3:
        st.metric(last_10days_data.iloc[2,0], metric3_value, delta3,delta_color= "inverse")

    with col4:
        st.metric(last_10days_data.iloc[3,0], metric4_value, delta4,delta_color="inverse")

    with col5:
        st.metric(last_10days_data.iloc[4,0], metric5_value, delta5,delta_color= "inverse")
    
##____________________________________________________________________________________________________________
## Gold suggestion    
    
    last_10days_data_check = last_10days_data.iloc[0]
    st.markdown("_________________________________________________________________________________")
    st.write("                                                                                       ")  
    st.markdown("<h2 style='color:black;font-size:22px;font-family:Arial;'>IS GOOD TO BUY GOLD TODAY?</h2>", unsafe_allow_html=True)
    if last_10days_data_check["PRICE_CHANGE(1gm-22K)"] < -50:
        st.success("Yes! it is good to buy GOLD today!!!")
        st.text( f"GOLD_RATE for 1gm-22K is {last_10days_data_check['GOLD_RATE(1gm-22K)']}, PRICE_CHANGE for 1gm-22K is {last_10days_data_check['PRICE_CHANGE(1gm-22K)']}")
    else:
        st.warning("It is good to wait for 2 more days to buy GOLD!")
        st.text( f" Because GOLD_RATE for 1gm-22K is ₹{last_10days_data_check['GOLD_RATE(1gm-22K)']}." + f" And PRICE_CHANGE for 1gm-22K is ₹{last_10days_data_check['PRICE_CHANGE(1gm-22K)']}")
 
        #st.text(f"And PRICE_CHANGE for 1gm-22K is ₹{last_10days_data_check['PRICE_CHANGE(1gm-22K)']}")

else:
    pass
    
##___________________________________________________________________________________________________________
## To form graph

if s == "Graphical Representation":
    
    
    gold_data_selected = last_10days_data[['DATE', 'GOLD_RATE(1gm-22K)']]
    max_index = gold_data_selected['GOLD_RATE(1gm-22K)'].idxmax()    
    
       
    #fig = px.bar(gold_data_selected, x='DATE', y='GOLD_RATE(1gm-22K)', title='Last 10 days Graph of gold price',color=gold_data_selected.index == max_index, color_discrete_map={False: 'blue', True: 'red'})
    #create a bar chart with Plotly Express
    fig = px.bar(gold_data_selected, x='DATE', y='GOLD_RATE(1gm-22K)', title='Last 10 days Graph of Gold Price in Chennai(Bar Chart)',color=gold_data_selected.index)
    fig.update_yaxes(range=[6000, 10000])   
    # Set the color of the bar corresponding to the maximum value to red
    fig.data[0].marker.color = ['red' if i == max_index else 'blue' for i in range(len(gold_data_selected))]
    st.plotly_chart(fig, use_container_width=True)
    
    fig2 = px.line(gold_data_selected, x='DATE', y='GOLD_RATE(1gm-22K)', title='Last 10 days Graph of Gold Price in Chennai(Line Chart)')
    fig2.update_yaxes(range=[6000, 10000])  # Set y-axis range from 0 to 10000

    # Display the line chart
    st.plotly_chart(fig2, use_container_width=True)

##_______________________________________________________________________________________________________________    

if s == "Feedback":
    st.markdown(" Kindly share your feedback here. Kindly provide rating in the scale of 1 to 10")
    #st.text("Is this website userfriendly")
    sb2 = st.slider(" * Is this website userfriendly?", 0,10,1)
    submit_button1 = st.button("Submit-1")
    if submit_button1:
        st.write("Your rating is", sb2)
    
    sb3 = st.slider(" * Is this website useful to analyse gold data?", 0,10,1)
    submit_button2 = st.button("Submit-2")
    if submit_button2:
        st.write("Your rating is", sb3)
    
    sb4 = st.slider(" * Overall rating for this website?", 0,10,1)
    submit_button3 = st.button("Submit-3") 
    if submit_button3:
        st.write("Overall your rating of this website for 20 is",  sb2+sb3)
    
    st.markdown("Thank you for your feedback! Keep Tracking!!")


