from fasthtml.common import *
from fasthtml import *

from get_jobs_from_google_sheets import get_jobs_from_google_sheets

css = Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

from dataclasses import dataclass

@dataclass
class Hero:
    title: str
    statement: str
    
    def __ft__(self):
        """ The __ft__ method renders the dataclass at runtime."""
        return Div(H1(self.title),P(self.statement), cls="hero")
    
def job_list(jobs):
    items = [job_row(row) for row in jobs[1:]]
    return Titled("List of jobs", Ul(*items))

def job_row(row):
    return Li(f"{row[0]} | {row[1]} | ", A('link', href=row[2]), f" | {row[3]} | {row[4]} | {row[5]}")

count = 0
# @rt("/")
@app.get("/")
def get():
    jobs = get_jobs_from_google_sheets()
    return Title("Cool Math Jobs"), Main(
        Titled("",
            Hero("Cool Math Jobs", "Find a fun job for your brain"), 
            Div(job_list(jobs)),
            P(f"Count is set to {count}", id="count"),
            Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")
        )
    )

@app.post("/increment")
def increment():
    print("incrementing")
    global count
    count += 1
    return f"Count is set to {count}"

serve()