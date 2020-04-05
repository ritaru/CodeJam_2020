// Original Code done by Ukjae Jeong
// @jeongukjae on Github (https://github.com/jeongukjae)

var {exec} = require("child_process");
var chalk = require("chalk");

const producer = exec("python local_testing_tool.py 0");
const consumer = exec("python ESAb_ATAd.py");

producer.stdout.on("data", (chunk) => {
  console.log(chalk.blueBright(("PRODUCER] " + chunk).trim()));
  consumer.stdin.write(chunk);
})

consumer.stdout.on("data", (chunk) => {
  console.log(("CONSUMER] " + chunk).trim());
  producer.stdin.write(chunk);
})

consumer.stderr.on("data", (chunk) => {
  console.log(chalk.green(("LOG] " + chunk).trim()));
})