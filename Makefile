DOCKER_IMAGES = $(shell docker images | grep badgepad | tr -s ' ' | cut -d ' ' -f 3 | uniq)
PWD = $(shell pwd)
TIMESTAMP = $(shell date +%s)
 
.PHONY: clean
clean:
	docker rmi $(DOCKER_IMAGES) --force
 
.PHONY: compile
compile:
	docker build -t badgepad:latest -t badgepad:$(TIMESTAMP) .
	docker run -ti --rm -v $(PWD)/output:/build -e KEYMAP=$(keymap) badgepad

.PHONY: force-compile
force-compile:
	docker build --no-cache -t badgepad:latest -t badgepad:$(TIMESTAMP) .
	docker run -ti --rm -v $(PWD)/output:/build badgepad

