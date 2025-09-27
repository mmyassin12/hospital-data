from pyspark.sql.functions import *

# Azure Event Hub Configuration
event_hub_host_name = "<<Nmaespace_hostname>>"
event_hub_name="<<Eventhub_name>>"  
event_hub_conn_str = "<<Connection_string>>"

kafka_options = {
    'kafka.bootstrap.servers': f"{event_hub_host_name}:9093",
    'subscribe': event_hub_name,
    'kafka.security.protocol': 'SASL_SSL',
    'kafka.sasl.mechanism': 'PLAIN',
    'kafka.sasl.jaas.config': f'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{event_hub_conn_str}";',
    'startingOffsets': 'latest',
    'failOnDataLoss': 'false'
}

#reading raw data from eventhub
raw_df = spark.readStream.format("kafka").options(**kafka_options).load()

#casting raw data to json
df_json = raw_df.selectExpr("CAST(value AS STRING) as raw_json")

#data lake configuration 
spark.conf.set(
  "fs.azure.account.key.<<Storage_accountname>>.dfs.core.windows.net",
  <<Storage_Account_Access_key>>
)

bronze_path = "abfss://<<Container_name>>@<<Storage_accountname>>.dfs.core.windows.net/<<path>>"

#write data to bronze layer
(df_json.writeStream.format("delta")
 .outputMode("append")
 .option("checkpointLocation", "abfss://bronze@hospitaldls.dfs.core.windows.net/_checkpoint/patient_data")
 .start(bronze_path))
