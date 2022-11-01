const { barSize, priceMap } = require(`${__dirname}/_dataload.js`)

// const barSize = 8
// const priceMap = [ 1, 5, 8, 9, 10, 17, 17, 20]

// const barSize = 6
// const priceMap = [1, 3, 11, 16, 19, 10]

console.time('runtime');

let mostProfit = {
    profits: new Array(barSize + 1),
    cuts: new Array(barSize + 1)
  } 

function cutBar() {
    mostProfit.profits[0] = 0
    for (bar = 1; bar <= barSize; bar++) {
        let profit = -1
        for (cut = 1; cut <= bar; cut++) {
            let value = priceMap[cut - 1] + mostProfit.profits[bar - cut]
            if (value > profit) {
                profit = value
                mostProfit.cuts[bar] = cut
            }
        }
        mostProfit.profits[bar] = profit
    }

    console.log(mostProfit.profits[barSize])
}

cutBar(barSize)
console.timeEnd('runtime');
console.log(`The most profitable way to divide the bar makes $${mostProfit.profits[barSize]} and is divided as follows:`)
let n = barSize
let pieces = 0
let value = mostProfit.cuts[n]
while (n > 0) {
    if (mostProfit.cuts[n] != value) {
        console.log(pieces + " of " + value)
        value = mostProfit.cuts[n]
        pieces = 0
    }
    pieces++
    n = n - mostProfit.cuts[n]
}

console.log(pieces + " of " + value)

