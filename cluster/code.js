
'use strict';
const http = require('http'),
    cluster = require('cluster'),
    os = require('os').cpus().length;

/*
 we will clone the cluster amount at the same time as the cores
 of the processor.
*/
if (cluster.isMaster) {
    for (let i = 0; i < os; i++) {
        cluster.fork();
        console.log(`The Worker number: ${i + 1} is alive`);
    }
    cluster.on('exit', (worker) => {
        console.log(`The Worker number: ${worker.id} has died`);
    });
} else {
    // we listen the same port
    http.createServer((sol, res) => {
        res.end('Hi, we are harnessing the power of clusters :)');
    }).listen(3000, () => console.log('The server is running on the port:3000'));
    console.log(`The Worker number: ${cluster.worker.id} is running`);
}