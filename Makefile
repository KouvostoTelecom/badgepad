DOCKER_IMAGES = $(docker images | grep badgepad | tr -s ' ' | cut -d ' ' -f 3)
PWD = $(shell pwd)

clean:
	echo $(DOCKER_IMAGES) 
	docker rmi $(DOCKER_IMAGES) --force

compile:
	docker build -t badgepad -t badgepad .
	docker run -ti --rm -v $(PWD)/output:/build badgepad

force-compile:
	docker build --no-cache -t badgepad -t badgepad .
	docker run -ti --rm -v $(PWD)/output:/build badgepad

