// Databricks notebook source
case class Person(name: String, age: Long)

// COMMAND ----------

val caseClasswaseem = Seq(Person("waseem", 25)).toDS().show

// COMMAND ----------

val peopleDS = spark.read.json("/FileStore/tables/people_json-501b6.txt").show()

// COMMAND ----------


