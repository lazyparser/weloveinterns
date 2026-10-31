all:
	echo "We Love Interns!"

# ---- 网站（weloveinterns.org） ----
site:
	hugo --source website --gc --minify --cleanDestinationDir

site-serve:
	hugo server --source website --disableFastRender --port 1314

site-check: site
	python3 scripts/check_site.py

site-clean:
	rm -rf website/public website/resources

help:
	@echo "type an action:"
	@echo "  all         默认，打印一句话"
	@echo "  site        构建站点到 website/public"
	@echo "  site-serve  本地预览 http://localhost:1314/"
	@echo "  site-check  构建后自检：站内链接、引用角标、来源登记"

.PHONY: all help site site-serve site-check site-clean
