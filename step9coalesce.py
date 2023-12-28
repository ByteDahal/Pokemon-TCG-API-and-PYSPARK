from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.functions import expr, monotonically_increasing_id

spark = SparkSession.builder.appName("pokemon_manipulation4").getOrCreate()


from step8exprAndPartition import sample_df

#coalesce bhanya partition lai optimize garni
#number of partition lai optimize garera performance dami banauni
#yedi partition ma 2 lekhya bhaye we don't need coalesce pachi
#dherai bhako partition ghatuni matra ho

# Assume sample_df has more than 2 partitions
sample_df = sample_df.coalesce(2)


# sample_df = sample_df.repartition(2, "hp"); yo lekhya bhaye coalesce(2) chaidaina

