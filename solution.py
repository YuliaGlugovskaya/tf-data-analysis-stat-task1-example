import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
chat_id = 206038589 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = 2*(x.mean() - 1)/(44*44)
    return a # Ваш ответ
