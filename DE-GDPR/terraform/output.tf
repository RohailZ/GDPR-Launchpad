output "lambda_function_name" {
  value = aws_lambda_function.gdpr_obfuscator.function_name
}

output "s3_bucket_name" {
  value = aws_s3_bucket.data_bucket.bucket
}
