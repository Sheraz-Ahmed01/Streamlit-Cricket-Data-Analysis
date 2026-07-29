import streamlit as st #streamlit is a front-end web framework of python
import pandas as pd #pandas is a data manipulation library
import plotly.express as px #dynamic visualization library of python
from streamlit_option_menu import option_menu #for the ppurpose of the navigator bar into web

st.cache_data.clear()
st.set_page_config(layout="wide")
st.title("Cric info app")

df=pd.read_csv("new_data.csv")

#st.dataframe(df)

select= option_menu(
    menu_title=None,
    options=["Home","Player Analysis","Country Insights","Comparison","Data Explorer","About"],
    icons=["house","person","globe","bar-chart","table","line"],
    orientation="horizontal"
)

##____Home Page____

if select=="Home":
    st.title("Cricket Analysis Dashboard")
    
    col1,col2,col3,col4=st.columns(4)

    col1.metric("Total Players",df['player'].nunique())
    col2.metric("Total Runs",df['Runs'].sum())
    col3.metric("Countries",df['country'].nunique())
    col4.metric("Total Matches",df['matches'].sum())
    st.dataframe(df.sample(10))


elif select=="Player Analysis":
    st.title("Player Analysis Stats")

    player=st.selectbox("Select Player",df['player'].unique())

    pdata=df[df['player']==player]

    df2=pdata[["matches","Inns","high_score","avg","balls_faced","strike_rate","100","50","0","4s","6s"]]
    df3=df2.T.reset_index()
    st.dataframe(df3)

    fig=px.bar(df3,x="index",y=df3.columns[1],color="index")
    

    df_pie=pdata[["100","50","6s","4s"]]
    pie1=df_pie.T.reset_index()
    fig_pie=px.pie(pie1,names="index",values=pie1.columns[1])
    
    col1,col2=st.columns(2)
    with col1:
        st.plotly_chart(fig,use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie,use_container_width=True)


    #st.dataframe(df2)


elif select=="Country Insights":
    st.title("Country Wise Analysis")

    scountry=st.selectbox("select country",df['country'].unique())
    
    col1,col2,col3,col4=st.columns(4)

    cdata=df[df["country"]==scountry]
    players=cdata["player"].nunique()
    total_runs=cdata["Runs"].sum()
    total_matches=cdata["matches"].sum()
    total_innings=cdata["Inns"].sum()

    col1.metric("Total Players",players)
    col2.metric("Total Runs",total_runs)
    col3.metric("Total Matches",total_matches)
    col4.metric("Total Tnnings",total_innings)
    
    df2=cdata[["player","Runs"]]
    df3=cdata[["player","Runs","matches","100","6s"]]
    df4=cdata[["Runs","matches","100","6s"]]

    fig=px.pie(df2,names="player",values="Runs")

    selectc=st.selectbox("select choice",df4.columns)

    fig2=px.bar(df3,x="player",y=selectc,color="player")

    st.plotly_chart(fig2,use_container_width=True)



elif select=="Comparison":
    st.title("Compare")

    player=st.multiselect("Compare Players",df["player"],default=df["player"].head(5))
    compare=df[df["player"].isin(player)]
    fig=px.scatter(
        compare,
        x="strike_rate",y="Runs",size="Runs",color="player",hover_name="country"
    )
    st.plotly_chart(fig,use_container_width=True)


elif select=="Data Explorer":
    st.title("Explore")

    st.dataframe(df)


elif select=="About":
    st.title("About The Author")

    st.info("About this Project")

    st.text("Project by: Sheraz Ahmed")

    st.success("End to End Streamlit Data Analysis Dashboard using Python for Cricket Analysis")

    col1,col2,col3,col4=st.columns(4)
    with col1:
        url="https://www.linkedin.com/in/sheraz-ahmed01/"
        st.link_button("Linkedin",url)
    with col2:
        url2="https://github.com/Sheraz-Ahmed01"
        st.link_button("Github",url2)














