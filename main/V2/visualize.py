import pandas as pd
import matplotlib.pyplot as plt

summary_df = pd.read_csv("./main/data/general/Summary.csv", sep="\t")

def visualize_results(summary_df):
    # Bar Chart: Success Rate
    plt.figure(figsize=(10, 6))
    plt.bar(summary_df["Model"], 
            [float(rate.strip('%')) for rate in summary_df["Success Rate"]], 
            color='blue')
    plt.title("Success Rate by Model")
    plt.ylabel("Success Rate (%)")
    plt.xlabel("Model")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Success_Rate.png")
    plt.show()

    # Bar Chart: Average Runtime
    plt.figure(figsize=(10, 6))
    plt.bar(summary_df["Model"], summary_df["Average Runtime (ms)"], color='green')
    plt.title("Average Runtime by Model")
    plt.ylabel("Runtime (ms)")
    plt.xlabel("Model")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Average_Runtime.png")
    plt.show()

    # Bar Chart: Average Memory Usage
    plt.figure(figsize=(10, 6))
    plt.bar(summary_df["Model"], summary_df["Average Memory Usage (bytes)"], color='red')
    plt.title("Average Memory Usage by Model")
    plt.ylabel("Memory Usage (bytes)")
    plt.xlabel("Model")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Average_Memory_Usage.png")
    plt.show()

if __name__ == "__main__":
    visualize_results(summary_df)
