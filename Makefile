IMAGE_NAME ?= "danduk82/qwc-init-postgresql"
IMAGE_TAG ?= "latest"

PHONY build:
build:
	@echo "Building..."
	@docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

PHONY build-no-cache:
build-no-cache:
	@echo "Building..."
	@docker build --no-cache -t $(IMAGE_NAME):$(IMAGE_TAG) .

PHONY push:
push:
	@echo "Pushing..."
	@docker push $(IMAGE_NAME):$(IMAGE_TAG)

PHONY clean:
clean:
	@echo "Cleaning..."
	@docker rmi $(IMAGE_NAME):$(IMAGE_TAG)