resource "aws_glue_job" "example_glue_job" {
  name          = "example_glue_job"
  role_arn      = aws_iam_role.glue_role.arn
  command       = "glueetl"
  script        = file("path/to/your/glue_script.py")  # Path to your PySpark script
  python_version = "3"

  # Additional Glue job settings, if needed
  # ...

  depends_on = [aws_iam_role.glue_role]
}

resource "aws_glue_trigger" "example_trigger" {
  name   = "example_trigger"
  type   = "SCHEDULED"
  schedule = "cron(0 0 * * ? *)"  # Example schedule: Daily at midnight UTC
  
  actions {
    job_name = aws_glue_job.example_glue_job.name
  }

  depends_on = [aws_glue_job.example_glue_job]
}
