#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle

const Rectangle = require('./4-rectangle');

const Square = class Square extends Rectangle {
	constructor(w, h, size) {
		super(w, h);
	}
	charPrint(c){
		let s = "";
		for (let i = 0; i < this.height; i++){
			s = "";
			for (let j = 0; j < this.width; j++){
				s += c ? c : "X";
			}
			console.log(s);
		}
	}
};

module.exports = Square;

