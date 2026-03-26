#!/bin/bash



docker stop mysite || true

docker rm mysite || true



docker build -t mysite .

docker run -d -p 80:80 --name mysite mysite
