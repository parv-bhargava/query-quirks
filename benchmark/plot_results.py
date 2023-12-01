# plot_results.py
import matplotlib.pyplot as plt

def plot_benchmark_results(times_data, query_names):
    plt.figure(figsize=(12, 8))
    for query_name in query_names:
        db_times = times_data[query_name]
        plt.plot(list(db_times.keys()), list(db_times.values()), marker='o', label=query_name)

    plt.title('Query Performance Benchmark Across Databases')
    plt.xlabel('Database')
    plt.ylabel('Time (seconds)')
    plt.legend(title='Query Names')
    plt.grid(True)
    plt.show()
