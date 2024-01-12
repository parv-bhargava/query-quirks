# QueryQuirks
"QueryQuirks" is a  GitHub project that focuses on the peculiar aspects or "quirks" of database queries by analyzing the performance of databases like SQL, MongoDB, Neo4J, and Hadoop. It benchmarks these systems using Python, focusing on efficiency metrics such as time, memory, and CPU usage, and offers insights for database optimization.

# Data Persistence and Performance Benchmarking Suite

## Abstract
This project offers a comparative performance analysis of four key database systems—SQL, MongoDB, Neo4J, and Hadoop—in the context of big data and cloud computing. Focusing on crucial metrics like time efficiency, memory usage, and CPU utilization, the study employs Python scripts to assess each system's operational performance. The findings indicate SQL's effectiveness in simple queries, MongoDB's consistent performance and scalability, Neo4J's memory efficiency with varying CPU demands, and Hadoop's proficiency in handling large-scale data. These insights provide valuable guidance for selecting and optimizing database technologies, addressing the diverse needs of database administrators, system architects, and developers.

## Introduction
In the era of big data and cloud computing, the performance of database systems is more crucial than ever. Businesses, researchers, and developers rely heavily on databases for storing, retrieving, and managing data efficiently. The choice of the right database technology can significantly impact the overall performance of an application, influencing factors such as response time, scalability, and resource utilization.

This project focuses on a comparative performance analysis of four widely used database systems: Structured Query Language (SQL), MongoDB, Neo4J, and Hadoop. Each of these systems offers unique features and is designed to meet different requirements in the realm of data management. SQL, a traditional relational database system, is known for its robust transactional integrity and structured query language. MongoDB, a NoSQL database, is celebrated for its flexibility and scalability in handling unstructured data. Neo4J, a graph database, excels in managing and querying complex relationships. Lastly, Hadoop, a distributed processing framework, is renowned for its capability to handle massive data sets across clustered systems.

The purpose of this project, "Data Persistence and Performance Benchmarking Suite," is to provide a comprehensive evaluation of these database systems. By focusing on key performance metrics such as time efficiency, memory usage, and CPU utilization, this study aims to offer a multi-dimensional view of how these databases operate under various data operations. This comparative analysis is not only crucial for database administrators and system architects but also invaluable for developers in making informed decisions when selecting a database technology that aligns with their specific needs and scenarios.

This project will detail the methodology employed in this study, present the findings of the performance benchmarks, and discuss the implications of these results in the broader context of data management strategies. Ultimately, this study aspires to be a pivotal resource in guiding the selection and optimization of database technologies across various industries and applications.

## Project Objective
The primary objective of this project, "Data Persistence and Performance Benchmarking Suite," is to conduct a thorough and comparative performance analysis of four major database systems: SQL, MongoDB, Neo4J, and Hadoop. These systems are pivotal in the current data management landscape, each offering unique functionalities and performance characteristics. The project aims to uncover these differences in performance through a series of structured benchmarks, focusing on three critical aspects:

1. **Time Efficiency:** Time efficiency is a crucial metric in database performance, particularly in environments where speed of data retrieval and manipulation directly impacts user experience and system efficiency. This study seeks to measure and compare the response times of each database system under a variety of conditions, ranging from simple data retrieval to complex data manipulation tasks. The aim is to understand how each database copes with different workloads and query complexities.
2. **Memory Usage:** Memory utilization is another vital aspect of database performance. Efficient memory usage not only ensures smooth operation but also affects the scalability and cost effectiveness of a system. This project will monitor and analyze the memory consumption patterns of each database during various operations. The objective is to provide insights into how each database manages memory under different loads and whether certain databases are more memory-efficient than others.
3. **CPU Utilization:** CPU usage is indicative of how computationally intensive operations are for a database. High CPU usage can be a bottleneck in performance, especially when handling complex queries or large volumes of data. This project aims to compare the CPU utilization of the four databases under study, thereby providing a perspective on their computational efficiency.
This information is crucial for understanding the suitability of each database for different types of applications, especially those with limited computational resources.

By achieving these objectives, this project intends to offer a comprehensive understanding of the performance dynamics of these database systems. The results are expected to guide database administrators, system architects, and developers in making informed choices about the right database technology for their specific requirements. Whether it's for a high-traffic web application, a complex data analytics task, or efficient handling of large-scale distributed data, this study aims to provide critical insights that will aid in the optimization of data management strategies across various industries and applications

## Methodology
The methodology for the "Data Persistence and Performance Benchmarking Suite" project is structured around a series of Python scripts designed to automate data loading, query execution, and performance measurement across four different database systems: SQL, MongoDB, Neo4J, and Hadoop.

### Python Scripts for Data Loading and Query Execution
1. **Data Loading Scripts (batch_load.py, load.py):** These scripts facilitate the loading of data into each of the databases. The load.py script appears to be the main entry point for initiating the data loading process. It uses batch_load.py scripts specific to each database, which include functions to handle data in batches, ensuring efficiency and manageability. For instance, the MongoDB loading script (batch_load.py) employs the pandas library to process data in chunks, inserting them into the database using the PyMongo driver.
2. **Query Execution Scripts (query_mongo.py, query_neo4j.py, query_sql.py):** These scripts contain functions to execute various types of queries specific to each database. They are designed to handle different query operations, such as find and aggregate in MongoDB. The scripts establish connections to their respective databases and execute the provided queries, returning the results or handling exceptions as needed.

### Benchmarking Process
1. **Benchmark Script (benchmarks.py):** The core benchmarking is conducted through the benchmarks.py script. This script is responsible for measuring and recording the performance metrics during query execution. It utilizes functions like measure_query_time to record the time taken for query execution, and employs the psutil library to monitor CPU and memory usage, providing a comprehensive view of each database’s performance.template.
2. **Design and Selection of Queries:** The queries are designed to test a wide range of functionalities, including data insertion, retrieval, updates, and complex relationships (especially in Neo4J). The choice of queries seems to be influenced by their relevance to real-world applications, ensuring that the benchmarking reflects practical scenarios.
3. **Performance Measurement Technique:**
    -  Time Measurement: The time taken by each query is measured using Python’s time module, allowing for precise measurement of execution duration.
    -  CPU and Memory Usage Measurement: The psutil library is used to monitor CPU and memory usage during the execution of queries. This approach provides insights into how each query impacts the system resources.
4. **Result Plotting Script (plot_results.py):** The plot_results.py script is used to visualize the results of the benchmarks. It generates plots for query times, CPU usage, and memory usage, enabling a clear and visual comparison across different databases and queries.
5. **Main Execution Script (main.py):** The main.py script is the driver script that orchestrates the benchmarking process. It calls the necessary functions to run benchmarks and plot results, ensuring a streamlined execution of the project.

### Database Systems Under Study
In this benchmarking project, we delve into four distinct database systems, each with its unique architecture and use cases. Understanding these systems' inherent characteristics is essential to comprehend the results and implications of our performance.

#### SQL (Structured Query Language) Database Systems
1. **Overview:** SQL databases, also known as Relational Database Management Systems (RDBMS), represent a traditional approach to data management. They use a structured query language for defining and manipulating data. SQL databases are characterized by their table-based structure, with data organized in rows and columns.
2. **Typical Use Cases:** These databases are ideal for applications requiring complex transactions, data integrity, and a structured schema. Examples include banking systems, CRM applications, and any system where data relationships and integrity are paramount.
3. **Key Characteristics:** SQL databases excel in ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring reliable transaction processing and data accuracy.
   
#### MongoDB
1. **Overview:** MongoDB is a leading NoSQL database known for its document-oriented approach. It stores data in JSON-like documents with dynamic schemas, offering more flexibility than traditional SQL databases.
2. **Typical Use Cases:** It is well-suited for applications that require rapid development, horizontal scalability, and the handling of diverse and unstructured data. Common examples include content management systems, real-time analytics, and applications dealing with large volumes of data without a fixed schema.
3. **Key Characteristics:** MongoDB is celebrated for its scalability, flexible schema design, and efficient handling of large volumes of diverse data.

#### Neo4J
1. **Overview:** Neo4J is a graph database designed for managing and querying complex networks of data. Its data
model is centred around nodes, relationships, and properties, making it highly efficient for relational analytics.
2. **Typical Use Cases:** This database is ideal for scenarios where relationships between data points are as crucial as the data itself. It finds extensive use in social networking applications, fraud detection, recommendation engines, and network and IT operations.
3. **Key Characteristics:** Neo4J excels in uncovering patterns and insights within connected data, offering high-performance traversal and querying of complex relationships.

#### Hadoop
1. **Overview:** Hadoop is not a database but a distributed file system (HDFS) and processing framework. It's included in this study due to its significant role in big data analytics and storage.
2. **Typical Use Cases:** Hadoop is predominantly used for storing and processing vast amounts of data in a distributed computing environment. It is ideal for applications requiring high throughput, fault tolerance, and scalability, such as big data analytics, data warehousing, and large-scale indexing.
3. **Key Characteristics:** Hadoop's strength lies in its ability to handle petabytes of data across multiple nodes, offering robust data processing capabilities and scalability.

Each of these systems brings distinct advantages and challenges to the table. By studying their performance under various conditions, this project aims to provide a nuanced understanding of their suitability for different data management requirements. This analysis will not only assist in selecting the appropriate technology for specific applications but will also contribute to the broader field of database management and optimization.

## Results and Analysis
[Add your results and analysis here]

### Time Efficiency Results
![Time Efficiency Results](URL-to-image)

#### For 50,000 records:
- SQL demonstrated superior time efficiency for select_basic and total_fare_over_2_miles queries but was significantly slower for the same_pickup_dropOff query.
- MongoDB showed consistently good performance across all queries, with the most notable efficiency in same_pickup_dropOff.
- Neo4j had varied results, with slower responses for select_basic and update_fare queries, but it was competitive for total_fare_over_2_miles.

#### For 100,000 records:
- The time efficiency for SQL decreased notably for same_pickup_dropOff, indicating a potential scalability issue with complex queries.
- MongoDB maintained consistent performance across the board, suggesting good scalability.
- Neo4j’s performance for select_basic queries degraded with more data, while it managed to handle update_fare more efficiently.

### Memory Usage Results
![Memory Usage Results](URL-to-image)

#### For 50,000 records:
- SQL consistently used more memory than MongoDB and Neo4j for all queries.
- MongoDB had a notable spike in memory for same_pickup_dropOff queries, suggesting an area for optimization.
- Neo4j showed the least memory usage overall, except for total_fare_over_2_miles where it peaked above SQL.

#### For 100,000 records:
- The pattern of memory usage for SQL and Neo4j remained like the 50,000 records case, with SQL using more memory.
- MongoDB’s memory usage pattern changed, with update fare now consuming more memory than the other queries.

### CPU Utilization Results
![CPU Utilization Results](URL-to-image)

#### For 50,000 records:
- SQL showed moderate CPU usage across all queries, with the least usage for update fare.
- MongoDB’s CPU usage was slightly higher than SQL’s for most queries except for same_pickup_dropOff.
- Neo4j had the highest CPU usage for select basic and update fare queries.

#### For 100,000 records:
- SQL's CPU usage pattern remained consistent, with only a slight increase across all queries.
- MongoDB displayed an increase in CPU usage for total_fare_over_2_miles and same_pickup_dropOff queries.
- Neo4j’s CPU usage increased for select basic but decreased for update fare, showing an unpredictable scaling pattern.

### Results and Analysis for Hadoop
Our examination of big data processing within the Hadoop ecosystem, utilizing PySpark, revealed insightful performance metrics across different scales. Queries were executed on datasets of 5 million and 24 million records to simulate realistic and challenging data processing scenarios. The metrics included the number of stages and tasks, elapsed time, executor run time, CPU time, JVM garbage collection time, shuffle write time, peak execution memory, as well as the records and bytes read. These measures offer a nuanced view of PySpark's performance characteristics.

- **Query 1:** demonstrated exceptional scalability. Despite increasing the dataset size from 5 million to 24 million records, the elapsed time decreased from 26 seconds to 23 seconds, suggesting efficient parallel processing and optimal use of cluster resources. The executor run time and CPU time also reflected a marginal decrease, further indicating that Query 1 is highly optimized for larger datasets.

- **Query 2:** showed increased elapsed time with larger data volumes, from 49 seconds for 5 million records to 43 seconds for 24 million records, implying a good scale but with diminishing returns as data size grows. Notably, the executor run time and CPU time saw a reduction, indicating that while the query took longer, it utilized resources more efficiently with the larger dataset.

- **Query 3:** presented a different pattern; it required more stages and tasks, which could indicate a more complex data processing operation. The elapsed time increased from 1.2 minutes to 56 seconds when scaling from 5 million to 24 million records, suggesting that the complexity of the query affects its scalability. Executor run time and CPU time both decreased, reflecting a more effective resource utilization at scale.

The JVM garbage collection time and shuffle write time were relatively low across all queries, suggesting that memory management and data shuffling were handled efficiently by PySpark. The peak execution memory was significantly higher for Query 3 on the 24 million record dataset, indicating a memory-intensive operation, likely due to the increased complexity and data size.

### Comparative Analysis
Performance Comparison Under Different Conditions
1. Scalability: MongoDB showed the least performance degradation when scaling from 50,000 to 100,000 records, indicating better scalability.
2. Complex Queries: SQL struggled with complex same_pickup_dropOff queries at scale, suggesting that query optimization may be required for larger datasets.
3. Read vs. Write Operations: Neo4j showed better performance in read operations (select_basic) for smaller datasets but had higher CPU usage for write operations (update_fare), particularly at scale.

### Strengths and Weaknesses of Each Database System in Various Scenarios
1. SQL:
    - Strengths: Good performance on simple read operations, lower memory usage at higher data volumes.
    - Weaknesses: Poor scalability for complex queries, higher memory usage for smaller datasets.
2. MongoDB:
    - Strengths: Consistent performance across different query types and scales, efficient in complex queries.
    - Weaknesses: Slight increase in CPU and memory usage as data volume grows.
3. Neo4j:
    - Strengths: Efficient memory usage in most scenarios, good performance in write operations at larger scales.
    - Weaknesses: High CPU usage, and performance inconsistency between read and write operations.

## Discussion
The benchmarking results highlight the nuanced performance profiles of SQL, MongoDB, and Neo4j across various operations. SQL databases showed proficiency in simple queries but faltered in more complex join operations at scale, indicating a potential trade-off between performance and complexity. MongoDB demonstrated a balance of time efficiency and scalability, maintaining consistent throughput across query types, suggesting its suitability for varied workloads. Neo4j excelled in memory efficiency, but its CPU usage patterns suggest a more cautious approach is needed when considering it for write-intensive applications.

These findings suggest that while no one database is universally superior, each has its own optimal use cases. SQL may be preferred for applications with simple transactions and queries, MongoDB for applications requiring flexible schema and rapid iteration, and Neo4j for relationship-heavy data with complex connections and patterns.

## Implications and Recommendations

### Implications:
1. **Workload-Specific Performance:** Different databases excel under different workloads. Understanding the specific demands of your application's queries and transactions is crucial for database selection.
2. **Scalability vs. Complexity:** As data volume increases, the complexity of queries can significantly affect performance. This is particularly true for SQL databases, which showed performance degradation with complex queries at higher volumes.
3. **Resource Utilization Balance:** The trade-off between CPU, memory, and execution time is critical. A database that performs well on one metric may consume more resources on another, affecting overall system efficiency.

### Recommendations:
1. **Targeted Benchmarking:** Prior to adopting a database, conduct benchmarks that closely mimic your application's expected workload, considering both current needs and future growth.
2. **Query Optimization:** For complex operations, particularly in SQL databases, invest in query optimization and indexing strategies to mitigate performance issues at scale.
3. **Architecture Alignment:** Align your system architecture with the database's strengths. For example, use Neo4j for data with complex relationships and MongoDB for applications that benefit from a flexible schema and rapid development cycles.
4. **Monitoring and Adaptation:** Implement robust monitoring to continually assess database performance. Be prepared to adapt, including potentially migrating to a different database, as your application's requirements evolve

By adhering to these recommendations, database administrators and system architects can make informed decisions that optimize performance and scalability, ensuring that the selected database system aligns with the specific needs of their applications.

## Conclusion
The comparative benchmarking analysis of SQL, MongoDB, Neo4j, and Hadoop databases provides a nuanced view into the performance dynamics of relational and NoSQL database systems. The key takeaways from the study are as follows:

- **SQL Databases:** They show strong performance for basic queries but face challenges with complex queries, especially as the dataset grows. This suggests that while SQL databases may be ideal for traditional applications with well-structured data and simple queries, they require careful consideration for applications that will scale significantly or involve complex joins and transactions.
- **MongoDB:** Exhibits consistent performance and handles scaling efficiently, making it a versatile option for a wide range of applications. Its flexibility with schema design and strong performance across different queries and scales make it suitable for applications that require rapid development and iteration, as well as those that will handle diverse and evolving data structures.
- **Neo4j:** Stands out for its efficient memory usage, particularly for operations that involve complex relationships and data patterns. However, its CPU usage for certain operations suggests that it may be best suited for read-heavy scenarios where relationship traversal is key.
- **Hadoop:** The results underscore the importance of optimizing query design and system architecture to harness Hadoop's full potential. This understanding is crucial as we move towards an era where the ability to process vast amounts of data efficiently is not just beneficial but essential for extracting valuable insights.

These findings contribute to the broader discourse in database technology selection and data management strategies by emphasizing the importance of context in database selection. Instead of seeking an all-encompassing solution, the study advocates for a strategic approach where the choice of database is driven by specific application needs, performance requirements, and long-term scalability considerations.

In sum, this benchmarking suite acts as a decision-support tool, guiding database administrators and system architects towards making data-driven choices. As the field of database technology continues to evolve, studies like this one are crucial in illuminating the path forward, ensuring that organizations can leverage the right database technologies to build efficient, scalable, and future-proof digital solutions.

## Acknowledgments
We express our deepest gratitude to Professor Hazim Shatnawi for their unwavering guidance, support, and mentorship throughout the duration of this project. Their expertise and encouragement significantly enriched our understanding and contributed to the success of this endeavor.

Additionally, we extend heartfelt appreciation to each member of our group whose dedication, collaboration, and diverse expertise were instrumental in the realization of this project. Our collective effort and synergy underscore the strength of teamwork and collaboration in achieving complex objectives.

## References
[Add your references here]

