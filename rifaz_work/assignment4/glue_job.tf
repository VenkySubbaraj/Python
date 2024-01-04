resource "aws_glue_job" "sample_assignment4_glue_job" {
  name          = "sample_assignment4_glue_job"
  role_arn      = "arn:aws:iam::667289912626:role/testing1_role"
  glue_version  = "4.0"
command {

    script_location = "s3://rifazdec24/pyspark/pyspark.py"
    python_version = "3"
  }
}

resource "aws_glue_trigger" "sample_assignment4_glue_job_trigger" {
  name   = "sample_assignment4_glue_job_trigger"
  type   = "SCHEDULED"
  schedule = "cron(0 6 * * ? *)" 
  
  actions {
    job_name = aws_glue_job.sample_assignment4_glue_job.name
  }
  depends_on = [aws_glue_job.sample_assignment4_glue_job]
}
