`define DUMPSTR(x) `"x.vcd`"
`timescale 1 ns / 10ps

module and_gate_tb();

//-- Leds port
wire [2:0] _LED;
reg [1:0] _BUT;

localparam DURATION = 1000;

//-- Instantiate the unit to test
and_gate UUT (
           .BUT(_BUT),
           .LED(_LED)
         );

initial begin
  // Time Changes
  _BUT[0] = 0;
  #10 _BUT[0] = 1;
  #20 _BUT[0] = 0;
  #30 _BUT[0] = 1;
end

initial begin

  $dumpfile(`DUMPSTR(`VCD_OUTPUT));
  $dumpvars(0, and_gate_tb);

  #(DURATION) $display("End of simulation");
  $finish;
end

endmodule