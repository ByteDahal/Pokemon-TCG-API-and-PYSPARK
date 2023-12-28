
# Continue with Spark session creation
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("pokemon_manipulation1").getOrCreate()



#aba load garni csv file in the spark session

file_path = r'./pokemon_cards.csv'
pokemon_df = spark.read.csv(file_path, header =True, inferSchema = True)
#yesma header = true matlab first line of csv is header of the column; column name bhaneko
#ani inferschema = true matlab without specifying data types python ley aafai placeholder use garera thah paii bhanya


#kei line of csv print garam hai ta
pokemon_df.show()

#kei random change hernu paryo bhaney let's create copy of this df
pokemon_df1 = pokemon_df

#aba kunai columns drop garnu paryo 
pokemon_df1.show()
pokemon_df1=pokemon_df1.drop("hp")
pokemon_df1.show()

#aba feri drop garya add garnu parey
pokemon_df1 = pokemon_df


#Aba rarity jata jata "Rare Holo" cha tei tei row ko data filter garnu parey

rare_holo_df = pokemon_df.filter(col("rarity")=="Rare Holo")
rare_holo_df.show()

# aba hamlai rare_holo_df ko csv chaiyo bhaney
output_path = r'./rare_holo1.csv'
pandas_df = rare_holo_df.toPandas()
pandas_df.to_csv(output_path, header=True, index=False)


output_path2 = r'./rare_holo.csv'
rare_holo_df.write.csv(output_path2, header=True, mode="overwrite")
# output_path2 = r'./rare_holo.parquet'
# rare_holo_df.write.parquet(output_path2, mode="overwrite")

#  header = true matlab first line lai header banaidini
#  mode= overwrite bhaneko pailai tyo file bhaye overwrite
