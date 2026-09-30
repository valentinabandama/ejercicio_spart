# Requisitos: pip install pyspark  +  Java 8/11/17 en el equipo
from pyspark.sql import SparkSession   # API moderna (PySpark 3 y 4)

# 1. CREAR la sesión: "local[*]" = todos los núcleos de tu PC
spark = SparkSession.builder \
    .appName("mi-primera-app") \
    .master("local[*]") \
    .getOrCreate()

# 2. LEER el archivo: un RDD donde cada elemento es una línea
rdd = spark.sparkContext.textFile("texto_python_1000_parrafos.txt")

# 3. TRANSFORMACIÓN (perezosa → NO se ejecuta todavía)
solo_python = rdd.filter(lambda l: "python" in l.lower())

# 4. ACCIÓN → aquí sí se ejecuta todo el plan
conteo = solo_python.count()

print("Líneas que mencionan 'python':", conteo)
spark.stop()