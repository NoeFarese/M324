TARGET = a.out
IMAGE_NAME = cpp_container

$(TARGET): main.cpp
	g++ -std=c++17 -o $(TARGET) main.cpp

docker-build: $(TARGET)
	docker build -t $(IMAGE_NAME) .
	@rm -f $(TARGET)

docker-run:
	docker run --rm $(IMAGE_NAME)

clean:
	docker rmi -f $(IMAGE_NAME)
