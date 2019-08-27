`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2016/05/02 21:01:18
// Design Name: 
// Module Name: testbench
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


module testbench_addsub;

wire    [7:0] S;
wire          C;
wire          V;
wire          N;
wire          Z;

reg     [7:0] A;
reg     [7:0] B;
reg           M;

wire    [7:0] S_VFY;
wire          C_VFY;
wire          V_VFY;
wire          N_VFY;
wire          Z_VFY;
wire    [7:0] B_mux;

integer i,j;


// Generate inputs
initial begin
  A = 8'b0;
  B = 8'b0;
  M = 1'b0;
  $display("Start AddSubtractor Simulation");
  $display("Testing Adder");
  #50;
  for(i=0;i<256;i=i+1) begin
    for(j=0;j<256;j=j+1) begin
      A = i;
      B = j;
      #10;
    end
  end

  M = 1'b1;
  $display("Testing Subtractor");
  #50;
  for(i=0;i<256;i=i+1) begin
    for(j=0;j<256;j=j+1) begin
      A = i;
      B = j;
      #10;
    end
  end
  $display("Simulation Finished"); 
  $display("All input combinations are verified!"); 
  $finish;
end

assign B_mux = (M ? ~B:B);

assign {C_VFY,S_VFY} = A+B_mux+M;
assign V_VFY = (~S_VFY[7]&A[7]&B_mux[7])|(S_VFY[7]&~A[7]&~B_mux[7]);
assign N_VFY = S_VFY[7];
assign Z_VFY = S_VFY==8'b0;

initial begin
  #55;
  forever begin
    if (S_VFY  != S) begin $display("S not matched"); $stop; end
    if (C_VFY  != C) begin $display("C not matched"); $stop; end
    if (V_VFY  != V) begin $display("V not matched"); $stop; end
    if (N_VFY  != N) begin $display("N not matched"); $stop; end
    if (Z_VFY  != Z) begin $display("Z not matched"); $stop; end
    #10;
  end
end

addsub U_ADDSUB
(
  .A    (A    ),
  .B    (B    ),
  .M    (M    ),
  .S    (S    ),
  .C    (C    ),
  .V    (V    ),
  .N    (N    ),
  .Z    (Z    )
);



endmodule
