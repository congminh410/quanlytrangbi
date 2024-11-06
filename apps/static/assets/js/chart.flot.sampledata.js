'use strict'

//\[\s+([0-9]+),\s+([0-9]+).([0-9]+)\s+],


var flotSampleData3 = [
  [0,36.57749563156254],
  [1,38.990117798360984],
  [2,42.33951429212372],
  [3,41.81299261981016],
  [4,37.43049180497279],
  [5,32.50742948537699],
  [6,28.15321230561721],
  [7,24.734038382708317],
  [8,23.48248771261796],
  [9,20.406002456692214]
];

var flotSampleData4 = [
  [0,53.08330533680049],
  [1,50.33339517545416],
  [2,49.4029746664779],
  [3,47.791939081203566],
  [4,49.09471219192674],
  [5,50.66529743518582],
  [6,48.749718825997206],
  [7,48.84333276982059],
  [8,53.51394720398375],
  [9,52.93467940905747],
];



function getRandomData(totalPoints = 10, start = 0) {
  var data = [];

  // Do a random walk
  while (data.length < totalPoints) {
    var prev = data.length > 0 ? data[data.length - 1] : start;
    var y = prev + Math.random() * 10 - 5;

    if(y < 0) { y = Math.random() * 10; }
    else if(y > 100) { y = 80; }

    data.push(y);
  }

  // Zip the generated y values with the x values
  var res = [];
  for (var i = 0; i < data.length; ++i) {
    res.push([i, data[i]])
  }

  return res;
}
