import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Spotify Data Dashboard", layout="wide")

st.title("🎵 דשבורד ניתוח נתוני ספוטיפיי")

uploaded_file = st.file_uploader("העלה קובץ נתוני ספוטיפיי (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("🔍 הקובץ נטען בהצלחה!")

    # תצוגת הנתונים הגולמיים
    with st.expander("הצג נתונים גולמיים"):
        st.dataframe(df)

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    st.sidebar.header("פילטרים")
    if 'year' in df.columns:
        year_min = int(df['year'].min())
        year_max = int(df['year'].max())
        year_selected = st.sidebar.slider("בחר שנה", year_min, year_max, (year_min, year_max))
        df = df[(df['year'] >= year_selected[0]) & (df['year'] <= year_selected[1])]
    
    if 'genre' in df.columns:
        genres = df['genre'].unique()
        selected_genres = st.sidebar.multiselect("בחר ז'אנרים", genres, default=list(genres))
        df = df[df['genre'].isin(selected_genres)]

    # סטטיסטיקות כלליות
    st.subheader("🎧 סטטיסטיקות כלליות")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("שירים בסך הכל", len(df))
    with col2:
        if 'artist' in df.columns:
            st.metric("אומנים שונים", df['artist'].nunique())
    with col3:
        if 'duration_ms' in df.columns:
            total_minutes = df['duration_ms'].sum() // (1000 * 60)
            st.metric("מוזיקה בדקות", total_minutes)

    # גרף פופולריות לפי שנה
    if "popularity" in df.columns and "year" in df.columns:
        st.subheader("פופולריות ממוצעת לפי שנה")
        popularity_by_year = df.groupby('year')['popularity'].mean()
        fig, ax = plt.subplots()
        popularity_by_year.plot(kind='bar', ax=ax)
        ax.set_ylabel("פופולריות ממוצעת")
        ax.set_xlabel("שנה")
        st.pyplot(fig)

    # ז'אנרים פופולריים
    if "genre" in df.columns and "popularity" in df.columns:
        st.subheader("10 הז'אנרים הפופולריים ביותר")
        top_genres = df.groupby("genre")["popularity"].mean().sort_values(ascending=False).head(10)
        fig2, ax2 = plt.subplots()
        top_genres.plot(kind="bar", ax=ax2, color='green')
        ax2.set_ylabel("פופולריות ממוצעת")
        ax2.set_xlabel("ז'אנר")
        st.pyplot(fig2)

    # קורלציה בין משתנים נומריים
    st.subheader("📊 מטריצת קורלציה בין מאפיינים נומריים")
    if len(numeric_columns) > 1:
        corr = df[numeric_columns].corr()
        st.dataframe(corr.style.background_gradient(cmap="RdYlGn"))

    # פלחי האמן הפופולרי
    if 'artist' in df.columns and 'popularity' in df.columns:
        st.subheader("10 האומנים הפופולריים ביותר")
        top_artists = df.groupby("artist")["popularity"].mean().sort_values(ascending=False).head(10)
        st.bar_chart(top_artists)

else:
    st.info("נא להעלות קובץ נתוני ספוטיפיי בפורמט CSV להמשך הניתוח.")