from fasthtml import common as fh
from utility_components import Hero, job_list, job_row
from dataclasses import dataclass

css = fh.Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')

def render(job):
    return fh.Card(fh.Li(f"{job.title} | {job.description} | {job.salary_range} | {job.why_is_cool} | ", fh.A('link', href={job.link})))

app, rt, jobs, Job = fh.fast_app('jobs.db', hdrs=(fh.picolink, css), live=True, render=render,
                        id=int,
                        title=str, 
                        description=str, 
                        link=str,
                        salary_range=str,
                        why_is_cool=str,
                        email=str,
                        pk='id'
                        )

submitted_jobs = []


count = 0
@rt("/")
def get():
    # # Generate random data
    # data = np.random.rand(5, 4)  # 5 rows and 4 columns
    # # Create a DataFrame with the random data
    # df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
    # jobs.insert(Job(title="Test job", 
    #                 description="cool job",
    #                 link="google.com",
    #                 salary_range="1-2 USD",
    #                 why_is_cool="because",
    #                 email="me@me.com" ))
    
    # return fh.Titled('Jobs',
    #               fh.Ul(*jobs()),
    #             )
    return fh.Title("Cool Math Jobs"), fh.Main(
        fh.Titled("",
            Hero("Cool Math Jobs", "Find a fun job for your brain"),
            fh.P(fh.A(fh.Button("Submit a job"), href="/submit_job")),
            fh.Card(fh.Ul(*jobs())),
            # fh.P(f"Count is set to {count}", id="count"),
            # fh.Button("Submit a job", hx_get="/submit_job", hx_target="#count", hx_swap="innerHTML"),
            
            # Div(NotStr(df.to_html())) 
        ), 
        cls="container"
    )

# @app.get("/submit_job")
@rt("/submit_job")
def get():
    frm = fh.Form(
        fh.Group(
            fh.Input(placeholder="job title", name='title'), 
            fh.Input(placeholder="description", name='description'), 
            fh.Input(placeholder="link", name='link'), 
            fh.Input(placeholder="salary range", name='salary_range'),
            fh.Input(placeholder="why is it cool", name='why_is_cool'),  
            fh.Input(placeholder="email", name='email'), 
            fh.Button("Submit")
            ), 
            hx_post='/submit_job'
        )
    return fh.Titled("Submit job", 
                fh.Main(fh.P("Submit a cool math job for consideration on the board:"),
                    fh.Card(fh.A(fh.Button("Go back to jobs"), href="/"), header=frm),
                )
            )
@rt("/submit_job")
def post(job:Job):
    # TODO: Add logic here to send me an email instead. 
    return jobs.insert(job)


@rt("/increment")
def post():
    print("incrementing")
    global count
    count += 1
    return f"Count is set to {count}"

fh.serve()
