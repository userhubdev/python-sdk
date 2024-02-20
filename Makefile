.PHONY: setup
setup:
	@sh -c "echo '#!/bin/sh\n\nmake lint test' > .git/hooks/pre-commit"
	@chmod 755 .git/hooks/pre-commit

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
