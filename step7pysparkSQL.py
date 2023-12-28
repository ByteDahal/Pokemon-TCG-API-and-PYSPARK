from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("pokemon_manipulation2").getOrCreate()

# file_path = r'./pokemon_cards.csv'
# pokemon_df = spark.read.csv(file_path, header=True, inferSchema=True)

from step6Pyspark import rare_holo_df

rare_holo_df.createOrReplaceTempView("table_name")
result = spark.sql("select * from table_name where hp > 100")
result.show()
spark.stop()