.PHONY: docker-build
IMAGE_NAME = ifconfig:latest

docker-build:
	docker build -t $(IMAGE_NAME) .

clean:
	docker rmi -f $(IMAGE_NAME)
