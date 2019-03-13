import pandas as pd
import read
data_hn = read.load_data()
#domain_count = data_hn["url"].value_counts()
#for name, row in domain_count[0:100].items():
    #print("{0}:{1}".format(name, row))
def subdom_remover(domain):
    dom = str(domain).split(".")
    if len(dom) == 3:
        dom_short = dom[1] + "." + dom[2]
        return dom_short
    if len(dom) == 2:
        dom_short = dom[0] + "." + dom[1]
        return dom_short
clean_domain = data_hn["url"].apply(subdom_remover)
domain_count = clean_domain.value_counts()
for name, row in domain_count[0:100].items():
    print("{0}:{1}".format(name, row))