import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data(num_samples=100):
    np.random.seed(0)
    data = np.random.randn(num_samples, 2)
    variable_1 = data[:, 0]
    variable_2 = data[:, 1]
    return variable_1, variable_2

def create_plots(variable_1, variable_2, figsize=(12, 10), title=None):
    sns.set(style="whitegrid")  # 그래프 스타일 설정
    
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    
    # 평균과 중앙값 그래프
    statistics = [("Mean", np.mean(variable_1), np.mean(variable_2)),
                  ("Median", np.median(variable_1), np.median(variable_2))]
    
    for i, (label, val_1, val_2) in enumerate(statistics):
        axes[0, 0].bar(label, val_1, color='blue' if i == 0 else 'green', alpha=0.7, label=f'Variable {i + 1}')
        axes[0, 0].bar(label, val_2, color='green' if i == 0 else 'blue', alpha=0.7)
    
    axes[0, 0].legend()
    axes[0, 0].set_title('Descriptive Statistics: Mean and Median')
    
    # 상관관계 히트맵
    corr_matrix = np.corrcoef(np.vstack((variable_1, variable_2)))
    sns.heatmap(corr_matrix, annot=True, ax=axes[0, 1], cmap="coolwarm", linewidths=0.5)
    axes[0, 1].set_title('Correlation Analysis')
    
    # 히스토그램 그래프
    for i, variable in enumerate([variable_1, variable_2]):
        axes[1, 0].hist(variable, bins=15, color='blue' if i == 0 else 'green', alpha=0.7, label=f'Variable {i + 1}')
    axes[1, 0].legend()
    axes[1, 0].set_title('Histogram of Variables')
    
    # 산점도 그래프
    axes[1, 1].scatter(variable_1, variable_2, alpha=0.7)
    axes[1, 1].set_xlabel('Variable 1')
    axes[1, 1].set_ylabel('Variable 2')
    axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')
    
    if title:
        plt.suptitle(title)  # 전체 그래프 제목 추가
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    variable_1, variable_2 = generate_data()
    create_plots(variable_1, variable_2, title="Data Analysis Result")

    # 각 그래프 상단에 어떤 그래프인지 표기
    create_plots(variable_1, variable_2, title="Mean and Median Graphs")
    create_plots(variable_1, variable_2, title="Correlation Heatmap")
    create_plots(variable_1, variable_2, title="Histogram Graphs")
    create_plots(variable_1, variable_2, title="Scatter Plot")
