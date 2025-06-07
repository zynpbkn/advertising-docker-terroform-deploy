terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "advertising_image" {
  name         = "advertising-fastapi:latest"
  build {
    context = "${path.module}"
  }
}

resource "docker_container" "advertising_container" {
  name  = "advertising_fastapi"
  image = docker_image.advertising_image.latest
  ports {
    internal = 8000
    external = 8002
  }
}