provider "local" {}

resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo 'Terraform executed'"
  }
}
