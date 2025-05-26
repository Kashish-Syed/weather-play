from preswald import connect, get_df
from preswald import query
from preswald import table, text

connect()
df = get_df("data/weather.csv")  # Load data

# Filter the data
sql = 'SELECT * FROM data/weather.csv where windy'
filtered_df = query(sql, "data/weather.csv")

text("# My Data Analysis App")
table(filtered_df, title="Avg Temp > 50°F")

from preswald import plotly
import plotly.express as px

# Create a bar chart of play decisions by outlook
fig = px.histogram(df, x="outlook", color="play", barmode="group", title="Play Decisions by Outlook")
plotly(fig)