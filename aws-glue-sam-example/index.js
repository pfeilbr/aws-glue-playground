const AWS = require('aws-sdk');

(async () => {

    const s3 = new AWS.S3();
    const resp = await s3.listBuckets().promise();
    console.log(JSON.stringify(resp, null, 2));

})()