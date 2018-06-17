#!/usr/bin/node
// created by goviraja on 01/12/2018 
// this requires - npm install ev3dev-lang

var ev3dev = require('ev3dev-lang');

// Run motor
console.log('Motor ----------------------------------');

// Pick the first connected motor
var motor = new ev3dev.Motor();

if (!motor.connected)
    console.log("No motor could be found. Are you sure that one is connected?");

console.log(' Port: ' + motor.address);
console.log(' Driver: ' + motor.driverName);
console.log(' Available commands: ' + motor.commands);

console.log('Sending motor command...');

motor.rampUpSp = 100;
motor.rampDownSp = 100;
motor.runForTime(10000, motor.maxSpeed / 2, motor.stopActionValues.brake);

do {
    console.log("Motor speed: " + motor.speed);
    
    {   
        var start = new Date().getTime();
        //console.log("time is: " + start);
        while (new Date().getTime() < start + 80) {
            ;
        }
    }
} while(motor.speed > 10);

console.log('-----------------------------------------------');
