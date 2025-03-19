import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_excel("C:/Users/Vanderson Vieira/Downloads/leads.xlsx", 'Sheet1')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file('output.html')