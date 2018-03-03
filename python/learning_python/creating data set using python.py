# Databricks notebook source
df = spark.read.json("/mnt/mylearningdata/people.json.txt")

# COMMAND ----------

df.show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.select("name").show()

# COMMAND ----------

df.select(df['name'], df['age'] ).show()

# COMMAND ----------

df.filter(df['age'] > 18).show()

# COMMAND ----------

df.groupBy("name").count().show()

# COMMAND ----------

df.createOrReplaceTempView("people")

# COMMAND ----------

sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()

# COMMAND ----------

df.createGlobalTempView("people")

# COMMAND ----------

spark.sql("SELECT * FROM global_temp.people").show()

# COMMAND ----------

case class Person(name: String, age: Long)

# COMMAND ----------


