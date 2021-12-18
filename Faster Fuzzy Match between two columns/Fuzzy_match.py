import pandas as pd
import numpy as np
import joblib,fuzzywuzzy
from fuzzywuzzy import fuzz,process
from joblib import Parallel, delayed
print("numpy vesrion::",np.__version__)
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

ca = np.array(df1[["Company A"]])
cb = np.array(df2[["Company B"]])

def parallel_fuzzy_match(idxa,idxb):
    return [ca[idxa][0],cb[idxb][0],metric(ca[idxa][0],cb[idxb][0])]    

results = Parallel(n_jobs=-1,verbose=1)(delayed(parallel_fuzzy_match)(idx1, idx2) for idx1 in range(len(ca)) for idx2 in range(len(cb)) \
                   if(metric(ca[idx1][0],cb[idx2][0]) > thresh))
                     
results = pd.DataFrame(results,columns = ["Company A","Company B","Score"])
