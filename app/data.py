from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_dataframe():
    file_path = r'C:\Users\avram\OneDrive\Desktop\TRG Week 38\dvn.us.txt'
    df = pd.read_csv(file_path, sep=None, engine='python')  # Adjust sep if needed
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