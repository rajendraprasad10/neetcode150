variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}

variable "versioning_enabled" {
  description = "Whether to enable versioning"
  type        = bool
  default     = true
}

variable "encryption_algorithm" {
  description = "The server-side encryption algorithm"
  type        = string
  default     = "AES256"
}

variable "tags" {
  description = "Tags to assign to the S3 bucket"
  type        = map(string)
  default     = {}
}
