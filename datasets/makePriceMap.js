const fs = require('fs')

module.exports = (barSize) => {
  const fileName = `single-bar-${barSize}.json`

  try {
    return require(`${__dirname}/stored/${fileName}`)
  } catch (ignore) {}

  const output = []
  for(var i = 1; i <= barSize; i++){
    const randomPrice = 1 + Math.floor(Math.random() * barSize * 10)
    output.push(randomPrice)
  }

  fs.writeFileSync(`${__dirname}/stored/${fileName}`, "[")
  for(var i = 0; i < output.length; i++){
    try{
      var outputStr = JSON.stringify(output[i]) + ((i === output.length - 1) ? "]" : ",")
      fs.appendFileSync(`${__dirname}/stored/${fileName}`, outputStr, (err) => {
        if(err){
          console.log(`appendFileSync error`)
          console.log(err)
          console.log(output[i])
        }
      })
    } catch (err){
      console.log(`unknown index: ${i}`)
      console.log(err)
      console.log(output[i])
      break;
    }
  }
  return output
}
