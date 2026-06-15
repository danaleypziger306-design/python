import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Titanic Dashboard", layout="wide")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

st.title("🚢 Titanic Dataset Dashboard")
st.markdown(
    """
    Explore the Titanic dataset. Use the filters in the sidebar to explore survival odds, demographics and more.
    """
)

# Sidebar filters
st.sidebar.header("Filters")
pclass = st.sidebar.multiselect(
    "Passenger Class",
    options=df['Pclass'].unique(),
    default=df['Pclass'].unique()
)

sex = st.sidebar.multiselect(
    "Sex",
    options=df['Sex'].unique(),
    default=df['Sex'].unique()
)

embarked = st.sidebar.multiselect(
    "Port of Embarkation",
    options=df['Embarked'].dropna().unique(),
    default=df['Embarked'].dropna().unique()
)

age_range = st.sidebar.slider(
    "Age Range",
    min_value=int(df['Age'].min()),
    max_value=int(df['Age'].max()),
    value=(int(df['Age'].min()), int(df['Age'].max()))
)

df_filtered = df[
    (df['Pclass'].isin(pclass)) &
    (df['Sex'].isin(sex)) &
    (df['Embarked'].isin(embarked)) &
    (df['Age'].between(age_range[0], age_range[1]))
]

# Key metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Passengers", len(df_filtered))
col2.metric("Survivors", int(df_filtered['Survived'].sum()))
col3.metric("Survival Rate", f"{100 * df_filtered['Survived'].mean():.2f}%")
col4.metric("Average Fare", f"${df_filtered['Fare'].mean():.2f}")

st.divider()

# Visualizations

# Survival by Sex
fig1 = px.histogram(
    df_filtered, x="Sex", color="Survived",
    barmode="group",
    histfunc="count",
    labels={"Survived": "Survived", "count": "Passengers"},
    title="Survival Count by Sex",
    category_orders={"Survived": [0, 1]}
)
fig1.update_layout(legend_title_text="Survived")

# Survival by Class
fig2 = px.histogram(
    df_filtered, x="Pclass", color="Survived",
    barmode="group",
    histfunc="count",
    labels={"Survived": "Survived", "count": "Passengers", "Pclass": "Passenger Class"},
    title="Survival Count by Passenger Class",
    category_orders={"Survived": [0, 1], "Pclass": sorted(df_filtered['Pclass'].unique())}
)
fig2.update_layout(legend_title_text="Survived")

# Fare distribution
fig3 = px.box(
    df_filtered, x="Survived", y="Fare", color="Survived",
    labels={"Survived": "Survived", "Fare": "Fare"},
    title="Fare Distribution by Survival"
)
fig3.update_xaxes(tickvals=[0, 1], ticktext=["No", "Yes"])
fig3.update_layout(showlegend=False)

# Age distribution
fig4 = px.histogram(
    df_filtered, x="Age", color="Survived",
    nbins=30, barmode="overlay",
    opacity=0.7,
    title="Age Distribution by Survival"
)
fig4.update_layout(legend_title_text="Survived")

# Layout
col5, col6 = st.columns(2)
col5.plotly_chart(fig1, use_container_width=True)
col6.plotly_chart(fig2, use_container_width=True)

col7, col8 = st.columns(2)
col7.plotly_chart(fig3, use_container_width=True)
col8.plotly_chart(fig4, use_container_width=True)

st.divider()
st.dataframe(df_filtered, use_container_width=True)