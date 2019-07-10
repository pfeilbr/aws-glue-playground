const AWS = require("aws-sdk");
const s3 = new AWS.S3();
const glue = new AWS.Glue();
const util = require("util");
const fs = require("fs");
const path = require("path");

require("dotenv").config();

const log = o => console.log(JSON.stringify(o, null, 2));
const sleep = (ms = 0) => new Promise(r => setTimeout(r, ms));
const timestampString = () => new Date().toISOString().replace(/:/g, ".");

const runGlueJob = async (jobBaseName, localScriptPath) => {
  const jobTimestampString = timestampString();
  const jobName = `${jobTimestampString}-${jobBaseName}`;
  const scriptBasename = path.basename(localScriptPath);
  const s3ScriptKey = `${
    process.env.SCRIPTS_DIRECTORY
  }/${jobTimestampString}-${scriptBasename}`;

  const s3PutObjectParams = {
    Bucket: process.env.BUCKET_NAME,
    Key: s3ScriptKey,
    Body: fs.readFileSync(localScriptPath)
  };
  const s3PutObjectResp = await s3.putObject(s3PutObjectParams).promise();
  log(s3PutObjectResp);

  const scriptLocation = `s3://${process.env.BUCKET_NAME}/${s3ScriptKey}`;
  const createJobParams = {
    Command: {
      Name: "pythonshell", // "glueetl",
      PythonVersion: "3", // or 2,
      ScriptLocation: scriptLocation
    },
    Name: jobName,
    Role: process.env.IAM_ROLE_NAME,
    MaxCapacity: 0.0625
  };
  log(createJobParams);

  const createJobResp = await glue.createJob(createJobParams).promise();
  log(createJobResp);

  const startJobRunParams = {
    JobName: jobName,
    MaxCapacity: 0.0625
  };
  const startJobRunResp = await glue.startJobRun(startJobRunParams).promise();
  log(startJobRunResp);

  const getJobRunParams = {
    JobName: jobName,
    RunId: startJobRunResp.JobRunId
  };

  const doneStatuses = "SUCCEEDED,STOPPED,FAILED,TIMEOUT".split(",");
  let getJobRunResp = await glue
    .getJobRun(getJobRunParams)
    .promise(getJobRunParams);

  while (!doneStatuses.includes(getJobRunResp.JobRun.JobRunState)) {
    getJobRunResp = await glue
      .getJobRun(getJobRunParams)
      .promise(getJobRunParams);
    log(getJobRunResp);
    await sleep(5000);
  }
};

const runPythonShellGlueJobExample = async () => {
  const scriptPath = path.join(
    __dirname,
    "..",
    "scripts",
    "python3-shell-job-example.py"
  );

  const jobBasename = path.basename(scriptPath, path.extname(scriptPath));
  await runGlueJob(jobBasename, scriptPath);
};

(async () => {
  await runPythonShellGlueJobExample();
})();
