`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2016/05/19 12:43:08
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

reg           rst;
reg           clk;
reg     [1:0] CtrlParity;

reg           TxDataEnA;
reg     [7:0] TxDataA;
wire          RxDataRdyA;
wire    [7:0] RxDataA;
wire          ErrorA;

reg           TxDataEnB;
reg     [7:0] TxDataB;
wire          RxDataRdyB;
wire    [7:0] RxDataB;
wire          ErrorB;

wire          net_B2A;
wire          net_A2B;

integer i,j;
integer wait_cycles;

initial begin
  clk <= 1'b0;
  forever #5 clk <= ~clk;
end

initial begin
  // Init
  rst <= 1'b0;
  CtrlParity <= 2'b0;
  TxDataEnA <= 1'b0; TxDataA <= 8'b0; TxDataEnB <= 1'b0; TxDataB <= 8'b0;
  #100;
  rst <= 1'b1;

  for(j=0;j<4;j=j+1) begin
    CtrlParity <= j[1:0];

    // sending data from UART_A to UART_B
    @(posedge clk);
    for(i=0;i<256;i=i+1) begin
      @(posedge clk);
      TxDataEnA <= 1'b1; TxDataA <= i[7:0];
      @(posedge clk);
      TxDataEnA <= 1'b0;
      wait_cycles <= 0;
      @(posedge clk);
      while(RxDataRdyB!==1'b1) begin
        wait_cycles <= wait_cycles + 1;
        if(ErrorB!==1'b0) begin
          $display("Error signal received from UART_B");
          $stop;
        end
        if(wait_cycles>100) begin
          $display("Fail to get RxDataRdy signal");
          $stop;
        end
        @(posedge clk);
      end
      if(RxDataB !== TxDataA) begin
        $display("Error");
        $display("TxData from UART_A : %x",TxDataA);
        $display("RxData at   UART_B : %x",RxDataB);
        $stop;
      end
    end
    #100;

    // sending data from UART_B to UART_A
    @(posedge clk);
    for(i=0;i<256;i=i+1) begin
      @(posedge clk);
      TxDataEnB <= 1'b1; TxDataB <= i[7:0];
      @(posedge clk);
      TxDataEnB <= 1'b0;
      wait_cycles <= 0;
      @(posedge clk);
      while(RxDataRdyA!==1'b1) begin
        wait_cycles <= wait_cycles + 1;
        if(ErrorA!==1'b0) begin
          $display("Error signal received from UART_A");
          $stop;
        end
        if(wait_cycles>100) begin
          $display("Fail to get RxDataRdy signal");
          $stop;
        end
        @(posedge clk);
      end
      if(RxDataA !== TxDataB) begin
        $display("Error");
        $display("TxData from UART_B : %x",TxDataB);
        $display("RxData at   UART_A : %x",RxDataA);
        $display("RxData at   UART_A : %x",RxDataA);
        $display("RxData at   UART_A : %x",RxDataA);
        $stop;
      end
    end
    #100;
  end
  $display("Simulation finished");
  $finish;
end

uart_netlist UART_A
(
  .rst          (rst          ),
  .clk          (clk          ),
  .CtrlParity   (CtrlParity   ),
  .TxDataEn     (TxDataEnA    ),
  .TxData       (TxDataA      ),
  .RxDataRdy    (RxDataRdyA   ),
  .RxData       (RxDataA      ),
  .Error        (ErrorA       ),
  .Rx           (net_B2A      ),
  .Tx           (net_A2B      )
);

uart_netlist_my UART_B
(
  .rst          (rst          ),
  .clk          (clk          ),
  .CtrlParity   (CtrlParity   ),
  .TxDataEn     (TxDataEnB    ),
  .TxData       (TxDataB      ),
  .RxDataRdy    (RxDataRdyB   ),
  .RxData       (RxDataB      ),
  .Error        (ErrorB       ),
  .Rx           (net_A2B      ),
  .Tx           (net_B2A      )
);

endmodule
