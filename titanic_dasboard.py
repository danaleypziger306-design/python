import streamlit as st

# אופציות סינון נוספות (פילטרים)
def sidebar_filters(df):
    st.sidebar.header("אפשרויות סינון נוספות")
    # טווח גילאים
    age_min, age_max = int(df['Age'].min()), int(df['Age'].max())
    age_range = st.sidebar.slider("טווח גילאים", min_value=age_min, max_value=age_max, value=(age_min, age_max))

    # נמלי עלייה לאונייה
    embark_options = df['Embarked'].dropna().unique().tolist()
    embarked = st.sidebar.multiselect("נמל עליית נוסע", options=embark_options, default=embark_options)

    # שרידות
    survived_option = st.sidebar.selectbox(
        "הצג נוסעים ששרדו / לא שרדו / כולם",
        options=["כולם", "שרדו", "לא שרדו"]
    )
    return age_range, embarked, survived_option
import pandas as pd
import plotly.express as px

# טען את הנתונים של הטיטאניק
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)

df = load_data()
print('hi'')
st.title("דאשבורד אנליזת הנוסעים של הטיטאניק 🚢")
st.markdown(
    """
    דאשבורד אינטראקטיבי להצגת תובנות מנתוני הנוסעים של הטיטאניק.
    """
)

# פילטר לפי מגדר ומחלקה
col1, col2 = st.columns(2)
with col1:
    gender = st.multiselect(
        "בחר מגדר",
        options=df['Sex'].unique(),
        default=list(df['Sex'].unique())
    )
with col2:
    pclass = st.multiselect(
        "בחר מחלקה",
        options=sorted(df['Pclass'].unique()),
        default=sorted(df['Pclass'].unique())
    )

filtered_df = df[(df['Sex'].isin(gender)) & (df['Pclass'].isin(pclass))]

st.subheader("נתוני נוסעים מסוננים")
st.dataframe(filtered_df)

# הצגת השרדות לפי מגדר
st.subheader("שיעור השרדות על פי מגדר")
survived_by_gender = filtered_df.groupby('Sex')['Survived'].mean().reset_index()
fig1 = px.bar(survived_by_gender, 
             x='Sex', y='Survived',
             labels={'Survived': 'שיעור השרדות', 'Sex': 'מגדר'},
             color='Sex',
             title='שיעור השרדות (%) לפי מגדר')
fig1.update_layout(yaxis_tickformat=".0%")
st.plotly_chart(fig1, use_container_width=True)

# הצגת פיזור גילאים לפי השרדות
st.subheader("פיזור גילאים לפי סטטוס השרדות")
fig2 = px.histogram(filtered_df, 
                    x="Age",
                    color="Survived",
                    barmode='overlay',
                    nbins=30,
                    labels={"Age": "גיל", "Survived": "שורד"},
                    title="פיזור גילאים על פי סטטוס (0=לא שרד, 1=שרד)")
st.plotly_chart(fig2, use_container_width=True)

# הצגת השרדות לפי מחלקה
st.subheader("שיעור השרדות על פי מחלקת נסיעה")
survived_by_class = filtered_df.groupby('Pclass')['Survived'].mean().reset_index()
fig3 = px.bar(survived_by_class, x='Pclass', y='Survived',
              labels={'Survived': 'שיעור השרדות', 'Pclass': 'מחלקה'},
              color='Pclass',
              title='שיעור השרדות (%) לפי מחלקת נסיעה')
fig3.update_layout(yaxis_tickformat=".0%")
st.plotly_chart(fig3, use_container_width=True)