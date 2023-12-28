from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.functions import expr, monotonically_increasing_id

spark = SparkSession.builder.appName("pokemon_manipulation3").getOrCreate()




data = [("Amrit", 25), ("Binit", 23), ("Amaan", 22)]
columns = ["name", "age"]

sample_df = spark.createDataFrame(data, columns)
sample_df.show()

sample_df = sample_df.withColumn("sn", monotonically_increasing_id())

transformed_sample_df = sample_df.select("sn", "name", expr("age+1 as AgePlusOne"))

transformed_sample_df.show()
#agePlusONe column bancha teha mathi diyeko bhanda naya age aaucha i.e 1 badera


#yedi euta column thapnu parey

sample_df = transformed_sample_df.withColumn("address", expr("CONCAT(name, '_Address')"))
#aba address column ma name_address aaucha ex: amrit_address, binit_address, amaan_address

sample_df.show()

sample_df = sample_df.repartition(2, "sn")
#partition garni "hp" ko adhar ma i.e same hp bhaka lai same partition ma rakhni
#2 nalekhey ni huncha but it is a good practice for optimization 2 means how many partition (not exactly though just optimization)


