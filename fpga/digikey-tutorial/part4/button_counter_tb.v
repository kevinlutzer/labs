`define DUMPSTR(x) `"x.vcd`"
`timescale 1 ns / 10ps

module button_counter_tb();

//-- Leds port
wire [2:0] LED;
reg [1:0] BUT;

localparam DURATION = 100;

//-- Instantiate the unit to test
button_counter UUT (
           .but(BUT),
           .led(LED)
         );

initial begin
  // Time Changes
  BUT = 2'b11; #5;
  BUT = 2'b10; #5;
  BUT = 2'b11; #5;
  BUT = 2'b10; #5;
  BUT = 2'b11; #5;
  BUT = 2'b10; #5;
  BUT = 2'b11; #5;
  BUT = 2'b10; #5;
  BUT = 2'b11; #5;
  BUT = 2'b11; #5;
  BUT = 2'b10; #5;
  BUT = 2'b11; #5;
  BUT = 2'b10; #5;
end

initial begin

  $dumpfile(`DUMPSTR(`VCD_OUTPUT));
  $dumpvars(0, button_counter_tb);

  #(DURATION) $display("End of simulation");
  $finish;
end

endmodule