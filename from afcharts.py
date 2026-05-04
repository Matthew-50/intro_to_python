import matplotlib.pyplot as plt

# Load gapminder dataset from plotly
from plotly.express.data import gapminder

# Set default theme
plt.style.use("afcharts.afcharts")

df = gapminder().query("country == 'United Kingdom'")

# Make the figure wider than the default (6.4, 4.8)
fig = plt.figure(figsize=(8.5, 4.8))

plt.plot(df["year"], df["lifeExp"])

plt.xlim([1950, 2010])
plt.ylim([0, 82])

fig