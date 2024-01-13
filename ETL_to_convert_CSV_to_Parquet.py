import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.context import SparkContext

from awsglue.dynamicframe import DynamicFrame


arguments = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(arguments['JOB_NAME'], arguments)
pushdown = "region in ('ca','gb','us')"

datasource = glueContext.create_dynamic_frame.from_catalog(database = "tubepulse_raw", table_name = "raw_statistics", transformation_ctx = "datasource", push_down_predicate = pushdown)

applymapping = ApplyMapping.apply(frame = datasource, mappings = [("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "long", "category_id", "long"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "long", "views", "long"), ("likes", "long", "likes", "long"), ("dislikes", "long", "dislikes", "long"), ("comment_count", "long", "comment_count", "long"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "boolean", "comments_disabled", "boolean"), ("ratings_disabled", "boolean", "ratings_disabled", "boolean"), ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"), ("description", "string", "description", "string"), ("region", "string", "region", "string")], transformation_ctx = "applymapping")
resolvechoice = ResolveChoice.apply(frame = applymapping, choice = "make_struct", transformation_ctx = "resolvechoice")
dropnullfields = DropNullFields.apply(frame = resolvechoice, transformation_ctx = "dropnullfields")
datasink = dropnullfields.toDF().coalesce(1)
df_final_output = DynamicFrame.fromDF(datasink, glueContext, "df_final_output")
datasink = glueContext.write_dynamic_frame.from_options(frame = df_final_output, connection_type = "s3", connection_options = {"path": "s3://tubepulse-cleansed-useast1-dev/youtube/raw_statistics/", "partitionKeys": ["region"]}, format = "parquet", transformation_ctx = "datasink")

job.commit()