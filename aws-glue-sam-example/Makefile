BUCKET_NAME=com.brianpfeil.my-glue-bucket
JOB_NAME="python3-shell-glue-2.0-job"
BUILD_DIR_NAME=build

clean:
	rm -fr $(BUILD_DIR_NAME)/

build: clean
	mkdir $(BUILD_DIR_NAME)
	zip -r $(BUILD_DIR_NAME)/package.zip . -x $(BUILD_DIR_NAME)/ -x node_modules/
	echo $(JOB_NAME)


deploy: build
	aws s3 cp $(BUILD_DIR_NAME)/package.zip s3://$(BUCKET_NAME)/package.zip
	aws s3 cp main.py s3://$(BUCKET_NAME)/main.py

run_job: deploy
	aws glue start-job-run --job-name $(JOB_NAME)

.PHONY: clean build deploy run_job