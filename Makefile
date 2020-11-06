all: publish

publish:
	git remote | xargs -I{} git push {} master

.PHONY: all publish
