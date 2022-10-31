const { barSize, priceMap } = require(`${__dirname}/_dataload.js`)

console.time('runtime');

var mostProfit = {
  totalBarProfit: 0,
  division: []
}

let cut = (barSize, smallestPeace = 1, division = []) => {
  for(let peaceSize=smallestPeace; peaceSize <= barSize; peaceSize++){
    var numPeaces = 1;
    do{
      var leftover = barSize - numPeaces * peaceSize

      if(leftover === 0){
        let peacesProfit = smallestPeace * priceMap[peaceSize - 1]
        let finalDivisionMap = [...division, {peaceSize, numPeaces, peacesProfit}]
        var finalTotalBarProfit = 0
        for(let divisionDetails of finalDivisionMap){
          finalTotalBarProfit += divisionDetails.peacesProfit
          if(finalTotalBarProfit > mostProfit.totalBarProfit){
            mostProfit.totalBarProfit = finalTotalBarProfit
            mostProfit.division = finalDivisionMap
          }
        }
        return;
      }
      if(leftover > 0 && smallestPeace + 1 <= leftover){
        let peacesProfit = smallestPeace * priceMap[peaceSize - 1]
        cut(leftover, smallestPeace + 1, [...division, {peaceSize, numPeaces, peacesProfit}])
      }

      numPeaces++;
    }
    while(numPeaces * peaceSize <= barSize)
  }
}

cut(barSize)
console.timeEnd('runtime');

console.log(`The most profitable way to divide the bar makes $${mostProfit.totalBarProfit} and is divided as follows:`)
for(let divisionDetails of mostProfit.division) {
  console.log(`${divisionDetails.numPeaces}x${divisionDetails.peaceSize} ($${divisionDetails.peacesProfit})`)
}