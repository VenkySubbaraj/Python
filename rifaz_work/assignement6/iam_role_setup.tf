resource "aws_iam_role" "glue_role" {
  name = "glue_role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "glue.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_glue_job" "sample_glue_job" {
  name          = "sample_glue_job"
  role_arn      = aws_iam_role.glue_role.arn
  command       = "glueetl"
  script        = file("path/to/your/glue_script.py")  # Path to your PySpark script
  python_version = "3"

  depends_on = [aws_iam_role.glue_role]
}
depends_on = [aws_glue_job.sample_glue_job]
}
