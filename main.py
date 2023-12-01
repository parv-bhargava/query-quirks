from benchmark import benchmark,plot_results

# Run benchmarks
times_data, query_names = benchmark.run_benchmarks()

# Plot the benchmark results
plot_results.plot_benchmark_results(times_data, query_names)
