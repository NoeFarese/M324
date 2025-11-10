TARGET = a.out
IMAGE_NAME = cpp_container:latest

$(TARGET): main.cpp
	g++ -std=c++17 -o $(TARGET) main.cpp

docker-build: $(TARGET)
	docker build -t $(IMAGE_NAME) .
	@rm -f $(TARGET)

clean:
	docker rmi -f $(IMAGE_NAME)
