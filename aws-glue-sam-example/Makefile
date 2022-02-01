JOB_NAME="python3-shell-glue-2.0-job"

build:
	rm -fr build/
	mkdir build
	zip -r build/package.zip . -x build/
	echo $(JOB_NAME)


deploy: build
	aws s3 cp build/package.zip s3://com.brianpfeil.my-glue-bucket/package.zip

run_job: deploy
	aws glue start-job-run --job-name $(JOB_NAME)

.PHONY: build deploy run_job