const AWS=require('ows-sdk');
AWS.config.update({
  region:"us-east-1"
})
const ses=new AWS.SES();

exports.handler=async(event)=>{
  const params={
    Destination:{
      ToAddresses:["2100032060cseh@gmail.com"]
    },
    Message:{
      Subject: {Data:"Test AWS SES"},
      Body:{
        Text:{Data: "Hello,\nThis is a test message\n\nBest Regards."}
      }
    },
    Source: 'abhayvk42@gmail.com'
  };
  await ses.sendEmail(params).promise().then(response=>{
    console.log("Successfully Sent.")
  }, error=>{
    console.log("Error!!")
  })

};
