# Hospital pateint data analysis using Azure
Azure PySpark Azure Data Factory Azure Synapse Python Databricks PowerBI Git

## Content 
#### Summary 
This project showcases a real-time healthcare data pipeline built on Azure.
It tracks and analyses patient movement across hospital departments.
Streaming data is ingested continuously and processed in Databricks using PySpark.
The refined data is stored in Azure Synapse SQL Pool.
This enables advanced analytics and interactive visualizations.
Overall, it provides actionable insights to improve hospital operations.
#### Visual outline
 <img width="972" height="600" alt="image" src="https://github.com/user-attachments/assets/f8a5f4a9-8082-4cf0-bc99-291ab4bed5b9" />

#### Goals
	Capture real-time patient data using Azure Event Hub.
	Process and refine data in Databricks following the Bronze–Silver–Gold architecture.
	Design a star schema in Azure Synapse SQL Pool for efficient querying.
	Build an interactive dashboard using Power BI
	Implement version control and collaboration through Git
#### Technologies
	Azure Event Hub – Ingest real-time streaming data.
	Azure Databricks – Perform ETL processing using PySpark.
	Azure Data Lake Storage – Stage both raw and curated datasets.
	Azure Synapse SQL Pool – Serve as the central data warehouse for analytics.
	Power BI – Develop interactive dashboards 
	Git – Manage version control.
#### Development Process
1.	Event Hub Configuration
Set up an Event Hub namespace along with a dedicated patient-flow hub.
 
2. Data Generation
Built a Python script to simulate patient data — including department details, wait times, and discharge status — and stream it to Event Hub.
3. Storage Configuration
Deployed Azure Data Lake Storage (ADLS Gen2) for data management.
Created separate containers for the Bronze, Silver, and Gold data layers.
 
4. Databricks Processing Workflow
•	Notebook 01: Ingests Event Hub streams into the Bronze layer.
•	Notebook 02: Performs data cleaning and schema validation.
•	Notebook 03: Aggregates data and constructs star schema tables.
 
 
5. Synapse SQL Pool Setup
Provisioned a Severless SQL Pool in Azure Synapse.
Executed schema creation and fact/dimension table scripts 
 
6. Version Control Integration
Implemented Git for version management.

#### Schema Design
The data in the Gold layer in Severless SQL Pool is structured using a star schema:
•	Fact Table: Fact_patient – Captures patient visit details, timestamps, wait durations, and discharge information.
•	Dimension Tables:
o	Dim_Department – Contains department-related attributes.
o	Dim_Patient – Stores patient demographic details.
#### Data Analysis
Synapse to Power BI Integration
•	Connected Azure Synapse SQL Pool to Power BI.
•	Imported the Fact and related Dimension tables.
•	Defined relationships to enable Star Schema–based analytics.
Dashboard Highlights
The key operational insights from the Dashboard, include:
•	Total Bed occupancy by gender.
•	Department-level KPIs such as average length of stay and total patient count.
•	Interactive filters and slicers for gender-based analysis.

 







