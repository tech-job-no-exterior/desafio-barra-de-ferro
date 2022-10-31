const { barSize, priceMap } = require(`${__dirname}/_dataload.js`)

console.time('runtime');

let mostProfit = {
  totalBarProfit: 0,
  division: []
}

let cut = (barSize, peaceSize = 1, division = [], totalBarProfit = 0) => {
  if(peaceSize > barSize) return
  for(; peaceSize <= barSize; peaceSize++){
    var numPeaces = 1;
    do{
      var leftover = barSize - numPeaces * peaceSize
      var peacesProfit = numPeaces * priceMap[peaceSize - 1]
      if(leftover === 0){
        if(totalBarProfit + peacesProfit > mostProfit.totalBarProfit){
          mostProfit.totalBarProfit = totalBarProfit + peacesProfit
          mostProfit.division = [...division, {peaceSize, numPeaces, peacesProfit}]
        }
        break;
      }
      if(leftover > 0){
        cut(leftover, peaceSize + 1, [...division, {peaceSize, numPeaces, peacesProfit}], totalBarProfit + peacesProfit)
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