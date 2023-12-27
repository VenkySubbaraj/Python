resource "aws_glue_job" "sample_glue_job" {
  name          = "sample_glue_job"
  role_arn      = "arn:aws:iam::667289912626:role/testing1_role"
  glue_version  = "4.0"
command {

    script_location = "s3://rifazdec24/pyspark.py"
    python_version = "3"
  }
}
