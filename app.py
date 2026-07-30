from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
df = pd.read_excel("sales.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df["revenue"] = (df["price"] - df["discount"]) * df["sold_unit"]
app = Dash(__name__)
app.layout = html.Div([

    html.H1(
        "Interactive Sales Analytics Dashboard"
    ),

    dcc.Dropdown(

        id="city",

        options=[
            {"label": city,
             "value": city}
            for city in sorted(df["city"].unique())
        ],

        value=df["city"].unique()[0]

    ),

    dcc.Graph(id="revenue_chart"),

    dcc.Graph(id="category_chart"),

    dcc.Graph(id="salesperson_chart")

])
@app.callback(

    Output("revenue_chart", "figure"),

    Output("category_chart", "figure"),

    Output("salesperson_chart", "figure"),

    Input("city", "value")

)
def update_dashboard(city):

    filtered = df[df["city"] == city]

    revenue = filtered.groupby(
        "item",
        as_index=False
    )["revenue"].sum()

    fig1 = px.bar(
        revenue,
        x="item",
        y="revenue",
        title="Revenue by Product"
    )

    category = filtered.groupby(
        "category",
        as_index=False
    )["sold_unit"].sum()

    fig2 = px.pie(
        category,
        names="category",
        values="sold_unit",
        title="Category Distribution"
    )

    sales = filtered.groupby(
        "salesperson",
        as_index=False
    )["revenue"].sum()

    fig3 = px.bar(
        sales,
        x="salesperson",
        y="revenue",
        title="Revenue by Salesperson"
    )

    return fig1, fig2, fig3
if __name__ == "__main__":
    app.run(debug=True)