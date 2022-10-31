const makePriceMap = require(`${__dirname}/../datasets/makePriceMap`)

const barSize = 10

console.time('datasets loaded')
const priceMap = makePriceMap(barSize)
console.timeEnd('datasets loaded')

module.exports = {
  barSize,
  priceMap
}