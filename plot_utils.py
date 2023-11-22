# plot_utils.py

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data():
    np.random.seed(0)
    data = np.random.randn(100, 2)
    variable_1 = data[:, 0]
    variable_2 = data[:, 1]
    return variable_1, variable_2

def create_plots(variable_1, variable_2):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    axes[0, 0].bar(['평균', '중앙값'], [np.mean(variable_1), np.median(variable_1)], color='blue', alpha=0.7)
    axes[0, 0].bar(['평균', '중앙값'], [np.mean(variable_2), np.median(variable_2)], color='green', alpha=0.7)
    axes[0, 0].legend()
    axes[0, 0].set_title('기술통계: 평균과 중앙값')
    
    sns.heatmap(np.corrcoef(np.vstack((variable_1, variable_2))), annot=True, ax=axes[0, 1])
    axes[0, 1].set_title('상관관계 분석')
    
    axes[1, 0].hist(variable_1, bins=15, color='blue', alpha=0.7, label='변수 1')
    axes[1, 0].hist(variable_2, bins=15, color='green', alpha=0.7, label='변수 2')
    axes[1, 0].legend()
    axes[1, 0].set_title('변수의 히스토그램')
    
    axes[1, 1].scatter(variable_1, variable_2, alpha=0.7)
    axes[1, 1].set_xlabel('변수 1')
    axes[1, 1].set_ylabel('변수 2')
    axes[1, 1].set_title('변수 1 대 변수 2 산점도')
    
    plt.tight_layout()
    plt.show()
