`timescale 1ps / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2016/05/26 19:47:01
// Design Name: 
// Module Name: uart_netlist_my
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


module uart_netlist_my
   (rst,
    clk,
    CtrlParity,
    TxDataEn,
    TxData,
    RxDataRdy,
    RxData,
    Error,
    Rx,
    Tx);
    
  input rst;
  input clk;
  input [1:0]CtrlParity;
  input TxDataEn;
  input [7:0]TxData;
  output reg RxDataRdy;
  output reg [7:0]RxData;
  output reg Error;
  input Rx;
  output Tx;
    
    reg           TxParity;
    reg           RxParity;  
    reg           TxCount;
    reg           RxCount;
    reg           TxBuf;
    reg           state;
    
    assign Tx = TxBuf;
    
    integer TxIndex;
    integer RxIndex;
 
    always @(posedge clk or negedge rst)
    begin
      if(~rst) begin
            TxBuf <= 1;
            TxIndex <= 0;
            TxCount <= 0;
      end
      else if(TxDataEn & TxIndex == 0) begin
            TxBuf <= 0;
            TxIndex = TxIndex + 1;
            TxCount = 0;
      end
      else if(TxIndex == 1) begin
            TxBuf <= TxData[0];
            TxIndex = TxIndex + 1;
            if(TxData[0] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 2) begin
            TxBuf <= TxData[1];
            TxIndex = TxIndex + 1;
            if(TxData[1] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 3) begin
            TxBuf <= TxData[2];
            TxIndex = TxIndex + 1;
            if(TxData[2] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 4) begin
            TxBuf <= TxData[3];
            TxIndex = TxIndex + 1;
            if(TxData[3] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 5) begin
            TxBuf <= TxData[4];
            TxIndex = TxIndex + 1;
            if(TxData[4] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 6) begin
            TxBuf <= TxData[5];
            TxIndex = TxIndex + 1;
            if(TxData[5] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 7) begin
            TxBuf <= TxData[6];
            TxIndex = TxIndex + 1;
            if(TxData[6] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 8) begin
            TxBuf <= TxData[7];
            TxIndex = TxIndex + 1;
            if(TxData[7] == 1) TxCount = !TxCount;
      end
      else if(TxIndex == 9) begin
            if(CtrlParity == 2 & TxCount == 0) TxBuf = 0;
            else if(CtrlParity == 2 & TxCount == 1) TxBuf = 1;
            else if(CtrlParity == 3 & TxCount == 0) TxBuf = 1;
            else if(CtrlParity == 3 & TxCount == 1) TxBuf = 0;
            TxIndex = 0;
      end
      else               TxBuf <= 1;
    end
    
    always @(posedge clk or negedge rst) begin
        if(~rst) begin
            state <= 1'b0;
            RxData <= 8'b0;
            Error <= 1'b0;
            RxDataRdy <= 1'b0;
            RxParity <= 1'b0;
            RxCount <= 1'b0;
        end
        else if(Rx == 1 & state == 0) begin
            RxIndex = 0;
            RxCount <= 0;
            RxDataRdy <= 0;
        end
        else if(Rx == 0 & state == 0) state <= 1;
        else if(state == 1 & RxIndex == 0) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[0] <= Rx;
            RxIndex = RxIndex + 1;
        end
        else if(state == 1 & RxIndex == 1) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[1] <= Rx;
            RxIndex = RxIndex +1;
        end
        else if(state == 1 & RxIndex == 2) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[2] <= Rx;
            RxIndex = RxIndex +1;
        end
        else if(state == 1 & RxIndex == 3) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[3] <= Rx;
            RxIndex = RxIndex +1;
        end
        else if(state == 1 & RxIndex == 4) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[4] <= Rx;
            RxIndex = RxIndex +1;
        end
        else if(state == 1 & RxIndex == 5) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[5] <= Rx;
            RxIndex = RxIndex +1;
        end
        else if(state == 1 & RxIndex == 6) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[6] <= Rx;
            RxIndex = RxIndex +1;
        end
        else if(state == 1 & RxIndex == 7) begin
            if(Rx == 1) RxCount = !RxCount;
            RxData[7] <= Rx;
            RxIndex = RxIndex +1;
        end                                            
        else if(RxIndex == 8 & state == 1) begin
            if(CtrlParity == 2 & RxCount == 0) RxParity = 0;
            else if(CtrlParity == 2 & RxCount == 1) RxParity = 1;
            else if(CtrlParity == 3 & RxCount == 0) RxParity = 1;
            else if(CtrlParity == 3 & RxCount == 1) RxParity = 0;
            if(CtrlParity !== 0 & CtrlParity !== 1 & RxParity !== Rx) Error <= 1;
            RxDataRdy = 1;
            RxIndex = RxIndex + 1;
        end
        else if(RxIndex == 9 & state == 1) begin
            if(Rx !== 1) Error <= 1;
            state <= 0;
            RxIndex = 0;
            RxCount <= 0;
            RxDataRdy <= 0;
        end
    end

endmodule
