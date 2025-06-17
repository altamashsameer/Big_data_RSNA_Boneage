from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when


spark = SparkSession.builder.appName("BoneAgeProcessing").enableHiveSupport().getOrCreate()


df = spark.read.csv("gs://altamash/boneage/boneage-training-dataset.csv", header=True, inferSchema=True)



df_clean = df.withColumn("gender_str", when(col("male") == 1, "boy").otherwise("girl")) \
             .dropna(subset=["boneage", "male"])


df_clean = df_clean.withColumn("age_group", 
    when(col("boneage") < 84, "baby")
   .when(col("boneage") < 156, "child")
   .otherwise("teen"))



gender_count = df_clean.groupBy("gender_str").count()
gender_count.write.mode("overwrite").csv("gs://altamash/output/gender_count")


avg_age_by_gender = df_clean.groupBy("gender_str").avg("boneage")
avg_age_by_gender.write.mode("overwrite").csv("gs://altamash/output/avg_boneage_by_gender")


age_group_count = df_clean.groupBy("age_group").count()
age_group_count.write.mode("overwrite").csv("gs://altamash/output/age_group_count")


df_clean.write.mode("overwrite").csv("gs://altamash/output/cleaned_boneage_data")

print("Processing complete. Output saved to GCS.")
