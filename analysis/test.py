import torch
import numpy
import pandas as pd
import json
def compute(cv):
    with open('./analysis/data/Alevel.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(row)
