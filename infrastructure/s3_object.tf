resource "aws_s3_bucket_object" "coding_spark" {
  bucket = aws_s3_bucket.deltalake.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../job_spark.py"
  etag   = filemd5("../job_spark.py")
}
