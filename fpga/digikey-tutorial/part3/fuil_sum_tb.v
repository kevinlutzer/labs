`define DUMPSTR(x) `"x.vcd`"
`timescale 1 ns / 10ps

module full_sum_tb();

//-- Leds port
wire _C_OUT, _S;
reg _C_IN, _A, _B;

localparam DURATION = 60;

//-- Instantiate the unit to test
full_sum UUT (
           .A(_A),
           .B(_B),
           .C_IN(_C_IN),
           .S(_S),
           .C_OUT(_C_OUT)
         );

initial begin

  // Time Changes
  _A = 0; _B = 0; _C_IN=0; #5;
  _A = 0; _B = 0; _C_IN=1; #5;
  _A = 0; _B = 1; _C_IN=0; #5;
  _A = 0; _B = 1; _C_IN=1; #5;
  _A = 1; _B = 0; _C_IN=0; #5;
  _A = 1; _B = 0; _C_IN=1; #5;
  _A = 1; _B = 1; _C_IN=0; #5;
  _A = 1; _B = 1; _C_IN=1; #5;

end

initial begin

  $dumpfile(`DUMPSTR(`VCD_OUTPUT));
  $dumpvars(0, full_sum_tb);

  #(DURATION) $display("End of simulation");
  $finish;
end

endmodule