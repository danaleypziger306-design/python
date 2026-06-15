import plotly.graph_objects as go

# נתונים לדוגמה של סוגי משקאות קלים קרים
drinks = [
    "קולה",
    "ספרייט",
    "פפסי",
    "פאנטה",
    "תפוזינה",
    "אייס תה",
    "מים בטעמים"
]
calories = [140, 130, 150, 120, 80, 60, 40]
sugar = [35, 33, 38, 32, 19, 15, 10]
price = [6, 6, 5, 5, 7, 8, 7]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=drinks,
    y=calories,
    name='קלוריות',
    marker_color='crimson',
    text=calories,
    textposition='auto'
))
fig.add_trace(go.Bar(
    x=drinks,
    y=sugar,
    name='גרם סוכר',
    marker_color='limegreen',
    text=sugar,
    textposition='auto'
))
fig.add_trace(go.Scatter(
    x=drinks,
    y=price,
    name='מחיר (₪)',
    marker=dict(color='royalblue', size=14),
    mode='lines+markers+text',
    text=price,
    textposition="top center"
))

fig.update_layout(
    title='השוואה בין סוגי משקאות קלים קרים 🥤',
    xaxis_title='סוג משקה',
    yaxis_title='ערך (קלוריות / גרם סוכר / ₪)',
    barmode='group',
    legend=dict(x=0.01, y=0.99, bordercolor='Black', borderwidth=1),
    template='plotly_white',
    font=dict(family="Arial", size=16),
    autosize=True,
    margin=dict(l=40, r=40, t=80, b=40),
    height=550
)

fig.show()