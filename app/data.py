from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Load the data
file_path = r'C:\Users\avram\OneDrive\Desktop\TRG Week 38\dvn.us.txt'
df = pd.read_csv(file_path)

# Drop the 'OpenInt' column
df = df.drop(columns=['OpenInt'])

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create three DataFrames for analysis
df1 = df[(df['Date'] >= '1992-03-17') & (df['Date'] <= '2000-12-31')]
df2 = df[(df['Date'] >= '2001-01-01') & (df['Date'] <= '2010-12-31')]
df3 = df[(df['Date'] >= '2011-01-01') & (df['Date'] <= '2017-11-10')]


@app.route('/')
def show_dataframe():
    file_path = r'C:\Users\avram\OneDrive\Desktop\TRG Week 38\dvn.us.txt'
    df = pd.read_csv(file_path, sep=None, engine='python')  # Adjust sep if needed
    df = df.drop(columns=['OpenInt'])
    df['Date'] = pd.to_datetime(df['Date'])
    html_table = df.to_html(index=False)
    return render_template_string("""
        <html>
        <head><title>DVN DataFrame</title></head>
        <body>
            <h2>DVN Data</h2>
            {{ table|safe }}
        </body>
        </html>
    """, table=html_table)

if __name__ == '__main__':
    app.run(debug=True)