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


module testbench;

reg     [7:0] A;
reg     [7:0] B;
wire          EQ;
wire          GT;
wire          LT;
wire          GE;
wire          LE;

wire          EQ_VFY;
wire          GT_VFY;
wire          LT_VFY;
wire          GE_VFY;
wire          LE_VFY;

integer i,j;


// Generate inputs
initial begin
  A = 8'b0;
  B = 8'b0;
  $display("Start Comparator Simulation"); 
  #50;
  for(i=0;i<256;i=i+1) begin
    for(j=0;j<256;j=j+1) begin
      A = i;
      B = j;
      #10;
    end
  end
  #50;
  $display("Simulation Finished"); 
  $display("All input combinations are verified!"); 
  $finish;
end

assign EQ_VFY = $signed(A)==$signed(B);
assign GT_VFY = $signed(A)> $signed(B);
assign LT_VFY = $signed(A)< $signed(B);
assign GE_VFY = $signed(A)>=$signed(B);
assign LE_VFY = $signed(A)<=$signed(B);

initial begin
  #55;
  forever begin
    if (EQ_VFY  != EQ) begin $display("EQ not matched"); $stop; end
    if (GT_VFY  != GT) begin $display("GT not matched"); $stop; end
    if (LT_VFY  != LT) begin $display("LT not matched"); $stop; end
    if (GE_VFY  != GE) begin $display("GE not matched"); $stop; end
    if (LE_VFY  != LE) begin $display("LE not matched"); $stop; end
    #10;
  end
end

comparator U_COMPARATOR(
  .A    (A    ),
  .B    (B    ),
  .EQ   (EQ   ),
  .GT   (GT   ),
  .LT   (LT   ),
  .GE   (GE   ),
  .LE   (LE   )
);

endmodule
