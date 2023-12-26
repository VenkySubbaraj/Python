resource "aws_glue_job" "sample_glue_job" {
  name          = "sample_glue_job"
  role_arn      = aws_iam_role.glue_role.arn
  command       = "glueetl"
  script        = file("path/to/your/glue_script.py")  # Path to your PySpark script
  python_version = "3"
}
