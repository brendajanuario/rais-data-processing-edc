variable "base_bucket_name" {
  type        = string
  default     = "datalake-tf"
  description = "datalake teste para receber os microdados rais e caged"
}

variable "enviroment" {
  default = "prod"
}

variable "account_number" {
  default = "309083126863"
}