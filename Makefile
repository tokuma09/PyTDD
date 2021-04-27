
NAME=project
VERSION=latest
IMG_W_TAG=${NAME}:${VERSION}

VOLUME=${shell pwd}
V2V=${VOLUME}:/root/project

build:
		@docker build  -t ${IMG_W_TAG} .
run:
		@docker run -it --rm -v ${V2V} ${IMG_W_TAG}
