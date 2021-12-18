import pandas as pd
import joblib,fuzzywuzzy
from fuzzywuzzy import fuzz,process
from joblib import Parallel, delayed
print("pandas vesrion::",pd.__version__)
print("fuzzywuzzy vesrion::",joblib.__version__)
print("joblib vesrion::",fuzzywuzzy.__version__)

df1 = pd.DataFrame({"Company A" :["FREDDIE AMERICAN GOURMET SAUCE","CITYARCHRIVER 2018 FOUNDATION",
                                 "GLAXOSMITHKLINE CONSUMER HEALTHCARE 2020","LACKEY SHEET METAL",
                                 "HELGET GAS PRODUCTS","ORTHOQUEST","PRIMUS STERILIZER COMPANY",
                                 "LACKEY SHEET,^METAL","ORTHOQUEST LLC 18", "PRIMUS STERILIZER COMPANY,[LLC]"] })

df2 = pd.DataFrame({"Company B" :["FREDDIE LEES AMERICAN GOURMET SAUCE","CITYARCHRIVER 2015 FOUNDATION",
                                 "GLAXOSMITHKLINE CONSUMER HEALTHCARE","FDA Company","LACKEY SHEET METAL",
                                 "PRIMUS STERILIZER COMPANY LLC",
                                 "Great Bend  KS","HELGET GAS PRODUCTS INC","ORTHOQUEST LLC",
                                 "PRIMUS STERILIZER","CITYARCHRIVER 2022 FOUNDATION"] })

## Define the fuzzy metric (uncomment any one of the metric)
metric = fuzz.ratio
#metric = fuzz.partial_ratio
#metric = fuzz.token_sort_ratio
#metric = fuzz.token_set_ratio

# Define Threshold for Metric
thresh = 80

def parallel_fuzzy_match(idxa,idxb):
    CompanyA = df1.loc[idxa,"Company A"] 
    CompanyB = df2.loc[idxb,"Company B"]
    matched_score=metric(CompanyA,CompanyB)  
    return [CompanyA,CompanyB,matched_score]    

results = Parallel(n_jobs=-1,verbose=1)(delayed(parallel_fuzzy_match)(idx1, idx2) for idx1 in df1.index for idx2 in df2.index \
                   if((metric(df1.loc[idx1,"Company A"] ,df2.loc[idx2,"Company B"]) > thresh) \
                      & (df1.loc[idx1,"Company A"].split(" ")[0] == df2.loc[idx2,"Company B"].split(" ")[0])) )
results = pd.DataFrame(results,columns = ["Company A","Company B","Score"])
