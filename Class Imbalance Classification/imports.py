import itertools 
from tqdm import tqdm
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import numpy as np
import random
RANDOM_SEED = 10
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)
import warnings
warnings.filterwarnings("ignore")
import shap
from sklearn.metrics import roc_auc_score,classification_report,roc_curve,confusion_matrix
import pandas as pd
