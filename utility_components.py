from fasthtml import *
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
