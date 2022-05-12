import pyspark
import unidecode
import re
from pyspark.sql import functions as f
from pyspark.sql import functions as f

rais_data = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .option('encoding', 'latin1')
    .load("s3://datalake-brenda-309083126863/raw-data/")
)

def rename_cols(rename_df):
    for column in rename_df.columns:
        new_column = column.replace('.', '_').replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')
        new_column = new_column.lower()
        new_column = unidecode.unidecode(new_column)
        rename_df = rename_df.withColumnRenamed(column, new_column)
    return rename_df

def cast_remun(df):
    for column in df.columns:
        if "vl_rem" in column:
            df = df.withColumn(column, f.regexp_replace(column, ',', '.').cast('double'))
    return df


df = rename_cols(rais_data)
df = cast_remun(df)

#create uf column
df = df.withColumn("uf", f.col("municipio").cast('string').substr(1,2).cast('int'))


(
    df
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy('uf')
    .save("s3://datalake-brenda-309083126863/staging/rais/")
)



