`define DUMPSTR(x) `"x.vcd`"
`timescale 100 ns / 10 ns

module and_gate_tb();

//-- Simulation time: 1us (10 * 100ns)
parameter DURATION = 10;

//-- Leds port
wire _LED;
reg _BUT;

//-- Clock signal. It is not used in this simulation
reg clk = 0;
always #0.5 clk = ~clk;

//-- Instantiate the unit to test
and_gate UUT (
           .BUT(_BUT),
           .LED(_LED)
         );

initial begin

  // Time Changes
  #5 _BUT = 1;
  #5 _BUT = 0;
  #5 _BUT = 1;
  #5 _BUT = 0;

  $dumpfile(`DUMPSTR(`VCD_OUTPUT));
  $dumpvars(0, and_gate_tb);

   #(DURATION) $display("End of simulation");
  $finish;
end

endmodule


# https://technobyte.org/testbench-in-verilog