import pandas as pd
import matplotlib.pyplot as plt

summary_df = pd.read_csv("./main/data/general/total-summary.csv", sep="\t")

def visualize_results(summary_df):
    dark_colors = {'success_rate': 'cyan', 'runtime': 'magenta', 'memory': 'orange'}
    edge_color = 'white'
    text_color = 'white'
    
    # Invert runtime and memory usage so that higher is better
    summary_df["Inverse Runtime"] = summary_df["Average Runtime (ms)"].max() - summary_df["Average Runtime (ms)"]
    summary_df["Inverse Memory"] = summary_df["Average Memory Usage (bytes)"].max() - summary_df["Average Memory Usage (bytes)"]
    
    # Sorting by Success Rate (descending)
    summary_df = summary_df.sort_values(by="Success Rate", key=lambda x: x.str.rstrip('%').astype(float), ascending=False)
    
    # Bar Chart: Success Rate
    plt.figure(figsize=(10, 6), facecolor='none')
    plt.bar(summary_df["Model"], 
            [float(rate.strip('%')) for rate in summary_df["Success Rate"]], 
            color=dark_colors['success_rate'], edgecolor=edge_color)
    plt.title("Success Rate by Model", color=text_color)
    plt.ylabel("Success Rate (%)", color=text_color)
    plt.xlabel("Model", color=text_color)
    plt.xticks(rotation=45, ha='right', color=text_color)
    plt.yticks(color=text_color)
    plt.gca().set_facecolor('none')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Success_Rate.png", transparent=True, edgecolor=edge_color)
    plt.show()
    
    # Sorting by Performance Score (descending)
    summary_df = summary_df.sort_values(by="Inverse Runtime", ascending=False)
    
    # Bar Chart: Inverted Average Runtime (Higher is better)
    plt.figure(figsize=(10, 6), facecolor='none')
    plt.bar(summary_df["Model"], summary_df["Inverse Runtime"], 
            color=dark_colors['runtime'], edgecolor=edge_color)
    plt.title("Performance Score by Model (Higher is Better)", color=text_color)
    plt.ylabel("Performance Score (based on Runtime)", color=text_color)
    plt.xlabel("Model", color=text_color)
    plt.xticks(rotation=45, ha='right', color=text_color)
    plt.yticks(color=text_color)
    plt.gca().set_facecolor('none')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Average_Runtime.png", transparent=True, edgecolor=edge_color)
    plt.show()
    
    # Sorting by Efficiency Score (descending)
    summary_df = summary_df.sort_values(by="Inverse Memory", ascending=False)
    
    # Bar Chart: Inverted Average Memory Usage (Higher is better)
    plt.figure(figsize=(10, 6), facecolor='none')
    plt.bar(summary_df["Model"], summary_df["Inverse Memory"], 
            color=dark_colors['memory'], edgecolor=edge_color)
    plt.title("Efficiency Score by Model (Higher is Better)", color=text_color)
    plt.ylabel("Efficiency Score (based on Memory Usage)", color=text_color)
    plt.xlabel("Model", color=text_color)
    plt.xticks(rotation=45, ha='right', color=text_color)
    plt.yticks(color=text_color)
    plt.gca().set_facecolor('none')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Average_Memory_Usage.png", transparent=True, edgecolor=edge_color)
    plt.show()

if __name__ == "__main__":
    visualize_results(summary_df)
