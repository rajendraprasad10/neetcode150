output "associate_public_ip_address" {
  value = aws_instance.test_instance.public_ip
}  

output "instance_id" {
  value = aws_instance.test_instance.id
}

output "instance_type" {
  value = aws_instance.test_instance.instance_type
}
