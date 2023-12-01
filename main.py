from benchmark import plot_results
from benchmark.benchmarks import run_benchmarks

def main():
    # Run benchmarks
    times_data, cpu_usage_data, memory_usage_data, error_data, query_names = run_benchmarks()

    # Visualize results
    if times_data:
        plot_results.plot_query_times(times_data, query_names)

    if cpu_usage_data:
        plot_results.plot_cpu_usage(cpu_usage_data, query_names)

    if memory_usage_data:
        plot_results.plot_memory_usage(memory_usage_data, query_names)

    if error_data:
        plot_results.plot_errors(error_data, query_names)

if __name__ == "__main__":
    main()
