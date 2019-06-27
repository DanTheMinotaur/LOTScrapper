from collector.Database import Database
from collector.PageParser import Parser
from datetime import datetime
from collector.Analyser import Analyser


test = Analyser()

res = test.analyse_lotto()

for r,v in res.items():
    print(r)
    print(v)