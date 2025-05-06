variable "aws_region" {
  default = "eu-west-2"
}

variable "lambda_function_name" {
  default = "gdpr-obfuscator"
}

variable "s3_bucket_name" {
  default = "gdpr-obfuscator-data-bucket"
}
