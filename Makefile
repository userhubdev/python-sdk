.PHONY: fmt
fmt:
	@hatch fmt

.PHONY: lint
lint:
	@hatch fmt --check

.PHONY: test
test:
	@hatch run test:pytest
	@hatch run test:mypy src
