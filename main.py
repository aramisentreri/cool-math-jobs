from fasthtml.common import *
from fasthtml import *
from utility_components import Hero, job_list, job_row
from get_jobs_from_google_sheets import get_jobs_from_google_sheets

css = Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

submitted_jobs = []

from dataclasses import dataclass
import pandas as pd 
import numpy as np 

    

count = 0
# @rt("/")
@app.get("/")
def home():
    # # Generate random data
    # data = np.random.rand(5, 4)  # 5 rows and 4 columns
    # # Create a DataFrame with the random data
    # df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
    jobs = get_jobs_from_google_sheets()
    return Title("Cool Math Jobs"), Main(
        Titled("",
            Hero("Cool Math Jobs", "Find a fun job for your brain"),
            Div(job_list(jobs)),
            P(f"Count is set to {count}", id="count"),
            Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML"),
            A("Link to submission page (to add jobs)", href="/submit_job"),
            # Div(NotStr(df.to_html())) 
        ), 
        cls="container"
    )

@app.get("/submit_job")
def submit_job():
    return Main(P("Submit a cool math job for consideration on the board:"),
                Form(Input(type="text", name="data"),
                     Button("Submit"),
                     action="/", method="post"))
@app.post("/")
def add_submitted_job(data:str):
    print(data)
    # TODO: Send an email with the details of the job to see if it's worthy
    return home()

@app.post("/increment")
def increment():
    print("incrementing")
    global count
    count += 1
    return f"Count is set to {count}"

serve()