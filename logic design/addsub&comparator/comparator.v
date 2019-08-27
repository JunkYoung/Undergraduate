`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2016/05/14 20:53:45
// Design Name: 
// Module Name: comparator
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module comparator
(
    A,
    B,
    EQ,
    GT,
    LT,
    GE,
    LE
);

input   [7:0] A;
input   [7:0] B;
output        EQ;
output        GT;
output        LT;
output        GE;
output        LE;

wire    [7:0] S;
wire          C;
wire          V;
wire          N;
wire          Z;
wire          Zi;
wire          w1, w2, w3, w4;
wire          M;

assign M = 1'b1;

addsub U1 (A, B, M, S, C, V, N, Z);

xor (w1, N, V);
not (w2, w1);
not (Zi, Z);
and (w3, w2, Zi);
or (w4, w1, Z);

assign EQ = Z;
assign GT = w3;
assign LT = w1;
assign GE = w2;
assign LE = w4;

endmodule
