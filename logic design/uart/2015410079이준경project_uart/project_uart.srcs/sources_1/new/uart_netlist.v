// Copyright 1986-2015 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2015.4 (win64) Build 1412921 Wed Nov 18 09:43:45 MST 2015
// Date        : Thu May 19 14:28:04 2016
// Host        : jun-PC running 64-bit Service Pack 1  (build 7601)
// Command     : write_verilog
//               C:/Users/jun/Documents/Lecture/2016_1/Project/Project2/project_uart/project_uart.srcs/sources_1/new/project_uart.v
// Design      : uart
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xc7z020clg484-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* STRUCTURAL_NETLIST = "yes" *)
module uart_netlist
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
  output RxDataRdy;
  output [7:0]RxData;
  output Error;
  input Rx;
  output Tx;

  wire \<const1> ;
  wire [1:0]CtrlParity;
  wire [1:0]CtrlParity_IBUF;
  wire Error;
  wire Error_OBUF;
  wire Rx;
  wire \RxBuf[7]_i_1_n_0 ;
  wire [2:0]RxCounter;
  wire \RxCounter[0]_i_1_n_0 ;
  wire \RxCounter[1]_i_1_n_0 ;
  wire \RxCounter[2]_i_1_n_0 ;
  wire \RxCounter[2]_i_2_n_0 ;
  wire [7:0]RxData;
  wire RxDataRdy;
  wire RxDataRdy_OBUF;
  wire [7:0]RxData_OBUF;
  wire RxOneCnt;
  wire RxOneCnt_i_1_n_0;
  wire [1:0]RxState_nxt;
  wire [1:0]RxState_r;
  wire \RxState_r[0]_i_2_n_0 ;
  wire Rx_IBUF;
  wire Tx;
  wire \TxBuf[0]_i_1_n_0 ;
  wire \TxBuf[1]_i_1_n_0 ;
  wire \TxBuf[2]_i_1_n_0 ;
  wire \TxBuf[3]_i_1_n_0 ;
  wire \TxBuf[4]_i_1_n_0 ;
  wire \TxBuf[5]_i_1_n_0 ;
  wire \TxBuf[6]_i_1_n_0 ;
  wire \TxBuf[7]_i_1_n_0 ;
  wire \TxBuf[8]_i_1_n_0 ;
  wire \TxBuf[9]_i_1_n_0 ;
  wire \TxBuf[9]_i_2_n_0 ;
  wire \TxBuf_reg_n_0_[1] ;
  wire \TxBuf_reg_n_0_[2] ;
  wire \TxBuf_reg_n_0_[3] ;
  wire \TxBuf_reg_n_0_[4] ;
  wire \TxBuf_reg_n_0_[5] ;
  wire \TxBuf_reg_n_0_[6] ;
  wire \TxBuf_reg_n_0_[7] ;
  wire \TxBuf_reg_n_0_[8] ;
  wire \TxBuf_reg_n_0_[9] ;
  wire [7:0]TxData;
  wire TxDataEn;
  wire TxDataEn_IBUF;
  wire [7:0]TxData_IBUF;
  wire Tx_OBUF;
  wire clk;
  wire clk_IBUF;
  wire clk_IBUF_BUFG;
  wire rst;
  wire rst_IBUF;

  IBUF \CtrlParity_IBUF[0]_inst 
       (.I(CtrlParity[0]),
        .O(CtrlParity_IBUF[0]));
  IBUF \CtrlParity_IBUF[1]_inst 
       (.I(CtrlParity[1]),
        .O(CtrlParity_IBUF[1]));
  OBUF Error_OBUF_inst
       (.I(Error_OBUF),
        .O(Error));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT5 #(
    .INIT(32'h33960000)) 
    Error_OBUF_inst_i_1
       (.I0(RxOneCnt),
        .I1(Rx_IBUF),
        .I2(CtrlParity_IBUF[0]),
        .I3(RxState_r[0]),
        .I4(RxState_r[1]),
        .O(Error_OBUF));
  LUT2 #(
    .INIT(4'h2)) 
    \RxBuf[7]_i_1 
       (.I0(RxState_r[0]),
        .I1(RxState_r[1]),
        .O(\RxBuf[7]_i_1_n_0 ));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[0] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[1]),
        .Q(RxData_OBUF[0]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[1] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[2]),
        .Q(RxData_OBUF[1]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[2] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[3]),
        .Q(RxData_OBUF[2]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[3] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[4]),
        .Q(RxData_OBUF[3]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[4] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[5]),
        .Q(RxData_OBUF[4]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[5] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[6]),
        .Q(RxData_OBUF[5]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[6] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxData_OBUF[7]),
        .Q(RxData_OBUF[6]));
  FDCE #(
    .INIT(1'b0)) 
    \RxBuf_reg[7] 
       (.C(clk_IBUF_BUFG),
        .CE(\RxBuf[7]_i_1_n_0 ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(Rx_IBUF),
        .Q(RxData_OBUF[7]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT3 #(
    .INIT(8'h04)) 
    \RxCounter[0]_i_1 
       (.I0(RxCounter[0]),
        .I1(RxState_r[0]),
        .I2(RxState_r[1]),
        .O(\RxCounter[0]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT4 #(
    .INIT(16'h0028)) 
    \RxCounter[1]_i_1 
       (.I0(RxState_r[0]),
        .I1(RxCounter[1]),
        .I2(RxCounter[0]),
        .I3(RxState_r[1]),
        .O(\RxCounter[1]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT5 #(
    .INIT(32'h00002888)) 
    \RxCounter[2]_i_1 
       (.I0(RxState_r[0]),
        .I1(RxCounter[2]),
        .I2(RxCounter[1]),
        .I3(RxCounter[0]),
        .I4(RxState_r[1]),
        .O(\RxCounter[2]_i_1_n_0 ));
  LUT1 #(
    .INIT(2'h1)) 
    \RxCounter[2]_i_2 
       (.I0(rst_IBUF),
        .O(\RxCounter[2]_i_2_n_0 ));
  FDCE #(
    .INIT(1'b0)) 
    \RxCounter_reg[0] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(\RxCounter[0]_i_1_n_0 ),
        .Q(RxCounter[0]));
  FDCE #(
    .INIT(1'b0)) 
    \RxCounter_reg[1] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(\RxCounter[1]_i_1_n_0 ),
        .Q(RxCounter[1]));
  FDCE #(
    .INIT(1'b0)) 
    \RxCounter_reg[2] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(\RxCounter[2]_i_1_n_0 ),
        .Q(RxCounter[2]));
  OBUF RxDataRdy_OBUF_inst
       (.I(RxDataRdy_OBUF),
        .O(RxDataRdy));
  LUT2 #(
    .INIT(4'h8)) 
    RxDataRdy_OBUF_inst_i_1
       (.I0(RxState_r[0]),
        .I1(RxState_r[1]),
        .O(RxDataRdy_OBUF));
  OBUF \RxData_OBUF[0]_inst 
       (.I(RxData_OBUF[0]),
        .O(RxData[0]));
  OBUF \RxData_OBUF[1]_inst 
       (.I(RxData_OBUF[1]),
        .O(RxData[1]));
  OBUF \RxData_OBUF[2]_inst 
       (.I(RxData_OBUF[2]),
        .O(RxData[2]));
  OBUF \RxData_OBUF[3]_inst 
       (.I(RxData_OBUF[3]),
        .O(RxData[3]));
  OBUF \RxData_OBUF[4]_inst 
       (.I(RxData_OBUF[4]),
        .O(RxData[4]));
  OBUF \RxData_OBUF[5]_inst 
       (.I(RxData_OBUF[5]),
        .O(RxData[5]));
  OBUF \RxData_OBUF[6]_inst 
       (.I(RxData_OBUF[6]),
        .O(RxData[6]));
  OBUF \RxData_OBUF[7]_inst 
       (.I(RxData_OBUF[7]),
        .O(RxData[7]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h0028)) 
    RxOneCnt_i_1
       (.I0(RxState_r[0]),
        .I1(Rx_IBUF),
        .I2(RxOneCnt),
        .I3(RxState_r[1]),
        .O(RxOneCnt_i_1_n_0));
  FDCE #(
    .INIT(1'b0)) 
    RxOneCnt_reg
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxOneCnt_i_1_n_0),
        .Q(RxOneCnt));
  LUT6 #(
    .INIT(64'h1555AAAA1555FFFF)) 
    \RxState_r[0]_i_1 
       (.I0(RxState_r[1]),
        .I1(RxCounter[2]),
        .I2(\RxState_r[0]_i_2_n_0 ),
        .I3(CtrlParity_IBUF[1]),
        .I4(RxState_r[0]),
        .I5(Rx_IBUF),
        .O(RxState_nxt[0]));
  LUT2 #(
    .INIT(4'h8)) 
    \RxState_r[0]_i_2 
       (.I0(RxCounter[0]),
        .I1(RxCounter[1]),
        .O(\RxState_r[0]_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT5 #(
    .INIT(32'h4000AAAA)) 
    \RxState_r[1]_i_1 
       (.I0(RxState_r[1]),
        .I1(RxCounter[2]),
        .I2(RxCounter[0]),
        .I3(RxCounter[1]),
        .I4(RxState_r[0]),
        .O(RxState_nxt[1]));
  FDCE #(
    .INIT(1'b0)) 
    \RxState_r_reg[0] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxState_nxt[0]),
        .Q(RxState_r[0]));
  FDCE #(
    .INIT(1'b0)) 
    \RxState_r_reg[1] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\RxCounter[2]_i_2_n_0 ),
        .D(RxState_nxt[1]),
        .Q(RxState_r[1]));
  IBUF Rx_IBUF_inst
       (.I(Rx),
        .O(Rx_IBUF));
  LUT2 #(
    .INIT(4'h2)) 
    \TxBuf[0]_i_1 
       (.I0(\TxBuf_reg_n_0_[1] ),
        .I1(TxDataEn_IBUF),
        .O(\TxBuf[0]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[1]_i_1 
       (.I0(TxData_IBUF[0]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[2] ),
        .O(\TxBuf[1]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[2]_i_1 
       (.I0(TxData_IBUF[1]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[3] ),
        .O(\TxBuf[2]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[3]_i_1 
       (.I0(TxData_IBUF[2]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[4] ),
        .O(\TxBuf[3]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[4]_i_1 
       (.I0(TxData_IBUF[3]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[5] ),
        .O(\TxBuf[4]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[5]_i_1 
       (.I0(TxData_IBUF[4]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[6] ),
        .O(\TxBuf[5]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[6]_i_1 
       (.I0(TxData_IBUF[5]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[7] ),
        .O(\TxBuf[6]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[7]_i_1 
       (.I0(TxData_IBUF[6]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[8] ),
        .O(\TxBuf[7]_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \TxBuf[8]_i_1 
       (.I0(TxData_IBUF[7]),
        .I1(TxDataEn_IBUF),
        .I2(\TxBuf_reg_n_0_[9] ),
        .O(\TxBuf[8]_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h7DD7D77DFFFFFFFF)) 
    \TxBuf[9]_i_1 
       (.I0(CtrlParity_IBUF[1]),
        .I1(\TxBuf[9]_i_2_n_0 ),
        .I2(TxData_IBUF[1]),
        .I3(TxData_IBUF[0]),
        .I4(TxData_IBUF[3]),
        .I5(TxDataEn_IBUF),
        .O(\TxBuf[9]_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h6996966996696996)) 
    \TxBuf[9]_i_2 
       (.I0(TxData_IBUF[4]),
        .I1(TxData_IBUF[2]),
        .I2(TxData_IBUF[7]),
        .I3(CtrlParity_IBUF[0]),
        .I4(TxData_IBUF[5]),
        .I5(TxData_IBUF[6]),
        .O(\TxBuf[9]_i_2_n_0 ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[0] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[0]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(Tx_OBUF));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[1] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[1]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[1] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[2] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[2]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[2] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[3] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[3]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[3] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[4] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[4]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[4] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[5] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[5]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[5] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[6] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[6]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[6] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[7] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[7]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[7] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[8] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[8]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[8] ));
  FDPE #(
    .INIT(1'b1)) 
    \TxBuf_reg[9] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(\TxBuf[9]_i_1_n_0 ),
        .PRE(\RxCounter[2]_i_2_n_0 ),
        .Q(\TxBuf_reg_n_0_[9] ));
  IBUF TxDataEn_IBUF_inst
       (.I(TxDataEn),
        .O(TxDataEn_IBUF));
  IBUF \TxData_IBUF[0]_inst 
       (.I(TxData[0]),
        .O(TxData_IBUF[0]));
  IBUF \TxData_IBUF[1]_inst 
       (.I(TxData[1]),
        .O(TxData_IBUF[1]));
  IBUF \TxData_IBUF[2]_inst 
       (.I(TxData[2]),
        .O(TxData_IBUF[2]));
  IBUF \TxData_IBUF[3]_inst 
       (.I(TxData[3]),
        .O(TxData_IBUF[3]));
  IBUF \TxData_IBUF[4]_inst 
       (.I(TxData[4]),
        .O(TxData_IBUF[4]));
  IBUF \TxData_IBUF[5]_inst 
       (.I(TxData[5]),
        .O(TxData_IBUF[5]));
  IBUF \TxData_IBUF[6]_inst 
       (.I(TxData[6]),
        .O(TxData_IBUF[6]));
  IBUF \TxData_IBUF[7]_inst 
       (.I(TxData[7]),
        .O(TxData_IBUF[7]));
  OBUF Tx_OBUF_inst
       (.I(Tx_OBUF),
        .O(Tx));
  VCC VCC
       (.P(\<const1> ));
  BUFG clk_IBUF_BUFG_inst
       (.I(clk_IBUF),
        .O(clk_IBUF_BUFG));
  IBUF clk_IBUF_inst
       (.I(clk),
        .O(clk_IBUF));
  IBUF rst_IBUF_inst
       (.I(rst),
        .O(rst_IBUF));
endmodule
