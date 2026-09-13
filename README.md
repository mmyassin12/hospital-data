# 🏥 Hospital Patient Data Analysis using Azure

<p align="center">
  <img src="https://img.shields.io/badge/Azure-Cloud-blue?logo=microsoftazure" alt="Azure Badge">
  <img src="https://img.shields.io/badge/PySpark-Big%20Data-orange?logo=apachespark" alt="PySpark Badge">
  <img src="https://img.shields.io/badge/Azure%20Data%20Factory-ETL%20Pipelines-0078D4?logo=microsoftazure" alt="Azure Data Factory Badge">
  <img src="https://img.shields.io/badge/Azure%20Synapse-Analytics-008AD7?logo=microsoftazure" alt="Azure Synapse Badge">
  <img src="https://img.shields.io/badge/Azure%20Databricks-Data%20Engineering-FF3621?logo=databricks" alt="Azure Databricks Badge">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi" alt="Power BI Badge">
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git" alt="Git Badge">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge">
</p>

---

## 📑 Table of Contents
1. [Summary](#-summary)
2. [Visual Outline](#-visual-outline)
3. [Project Goals](#-project-goals)
4. [Technologies Used](#-technologies-used)
5. [Development Process](#️-development-process)
6. [Schema Design](#-schema-design)
7. [Data Analysis](#-data-analysis)
8. [Key Learnings](#-key-learnings)
9. [License](#-license)
10. [Author](#-author)

---

## 📘 Summary
This project showcases a **real-time healthcare data pipeline** built on Microsoft Azure.  
It tracks and analyzes **patient movement across hospital departments**, providing insights into operational efficiency.

Streaming data is ingested continuously and processed in **Databricks using PySpark**.  
The refined data is stored in **Azure Synapse SQL Pool**, enabling **advanced analytics** and **interactive Power BI dashboards**.

Overall, this solution delivers **actionable insights** to improve hospital workflows and resource utilization.

---

## 🧭 Visual Outline
<p align="center">
<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/9d69deb1-894e-4b23-9d23-3e13d3829a56" />


---

## 🎯 Project Goals
- Capture real-time patient data using **Azure Event Hub**.  
- Process and refine data in **Databricks** following the **Bronze–Silver–Gold** architecture.  
- Design a **star schema** in **Azure Synapse SQL Pool** for efficient querying.  
- Build an **interactive dashboard** in **Power BI**.  
- Implement **version control and collaboration** via Git.  

---

## 🧩 Technologies Used
| Technology | Purpose |
|-------------|----------|
| **Azure Event Hub** | Ingest real-time streaming data |
| **Azure Databricks** | Perform ETL processing using PySpark |
| **Azure Data Lake Storage (Gen2)** | Store raw and curated datasets |
| **Azure Synapse SQL Pool** | Central data warehouse for analytics |
| **Power BI** | Create interactive dashboards |
| **Git Bash** | Version control and collaboration |

---

## ⚙️️ Development Process

### 1️⃣ Event Hub Configuration
Set up an Event Hub namespace with a dedicated **patient-flow hub**.

<p align="center">
  <img width="908" height="475" src="https://github.com/user-attachments/assets/b5bf2d7b-b740-4245-b223-a473d1154837" alt="Event Hub Configuration">
</p>

---

### 2️⃣ Data Generation
Developed a **Python script** to simulate patient data — including department details, wait times, and discharge status — and stream it to **Event Hub**.

---

### 3️⃣ Storage Configuration
Deployed **Azure Data Lake Storage (ADLS Gen2)** for data management.  
Created separate containers for the **Bronze**, **Silver**, and **Gold** data layers.

<p align="center">
  <img width="909" height="409" src="https://github.com/user-attachments/assets/b1b7adae-cac7-473b-9b32-5c5de011f823" alt="ADLS Configuration">
</p>

---

### 4️⃣ Databricks Processing Workflow
- **Notebook 01:** Ingest Event Hub streams into the **Bronze** layer.  
- **Notebook 02:** Perform **data cleaning and schema validation**.  
- **Notebook 03:** Aggregate data and build **Star Schema tables**.  

<p align="center">
  <img width="938" height="461" src="https://github.com/user-attachments/assets/14b392ff-9650-42c6-938f-53eb8aaa4490" alt="Databricks Workflow 1">
</p>

<p align="center">
  <img width="940" height="419" src="https://github.com/user-attachments/assets/3f895971-464b-4a86-9294-3484e8540be1" alt="Databricks Workflow 2">
</p>

---

### 5️⃣ Synapse SQL Pool Setup
- Provisioned a **Serverless SQL Pool** in Azure Synapse.  
- Executed schema creation and fact/dimension table scripts.

<p align="center">
  <img width="940" height="442" src="https://github.com/user-attachments/assets/1a81a73a-77ff-4179-816e-6b968bd4488a" alt="Synapse Setup">
</p>

---

### 6️⃣ Version Control Integration
Used **Git Bash** for version control and collaboration across development workflows.

---

## 🧮 Schema Design
The **Gold layer** in the **Serverless SQL Pool** follows a **Star Schema** structure.

### Fact Table
- **Fact_Patient** – Captures patient visit details, timestamps, wait durations, and discharge info.

### Dimension Tables
- **Dim_Department** – Department-related attributes.  
- **Dim_Patient** – Patient demographic details.

---

## 📊 Data Analysis

### 🔗 Synapse → Power BI Integration
- Connected **Azure Synapse SQL Pool** to **Power BI**.  
- Imported Fact and Dimension tables.  
- Defined relationships for **Star Schema–based analytics**.

### 📈 Dashboard Highlights
- **Total Bed Occupancy** by gender.  
- **Department-level KPIs** – Average length of stay, total patient count.  
- **Interactive filters and slicers** for gender-based analysis.

<p align="center">
  <img width="1016" height="542" src="https://github.com/user-attachments/assets/de3c87a8-fa74-4a67-a907-918859ffe549" alt="Power BI Dashboard">
</p>

---

## 🧠 Key Learnings
- Implementing **streaming data pipelines** using Azure-native tools.  
- Designing **modular ETL workflows** in Databricks with PySpark.  
- Applying **Data Lakehouse principles** (Bronze–Silver–Gold).  
- Enabling **business intelligence** with Power BI and Synapse integration.  

---

## 🪪 License
This project is open-source and available under the **MIT License**.

---

## 🌐 Author
**Mohamud  Yassin**  
💼 Data Engineer | ☁️ Azure Enthusiast   
📫 Reach me at: mmyassin12@gmail.com
