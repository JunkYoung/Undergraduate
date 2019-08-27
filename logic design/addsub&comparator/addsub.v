`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2016/05/14 20:48:51
// Design Name: 
// Module Name: addsub
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


module addsub
(
  A,
  B,
  M,
  S,
  C,
  V,
  N,
  Z
);

input   [7:0] A;
input   [7:0] B;
input         M;
output  [7:0] S;
output        C;
output        V;
output        N;
output        Z;

wire    [7:0] Bi;
wire    [7:0] Cs;

xor (Bi[0], B[0], M);
xor (Bi[1], B[1], M);
xor (Bi[2], B[2], M);
xor (Bi[3], B[3], M);
xor (Bi[4], B[4], M);
xor (Bi[5], B[5], M);
xor (Bi[6], B[6], M);
xor (Bi[7], B[7], M);

assign C = Cs[7];

full_adder U0 [7:0] (A,Bi,{Cs[6:0],M},S,Cs);

assign N = S[7];
xor (V, Cs[6], Cs[7]);
nor (Z, S[0], S[1], S[2], S[3], S[4], S[5], S[6], S[7]);

endmodule
