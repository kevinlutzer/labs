//------------------------------------------------------------------
//-- Hello world example for the iCE40-HX8K board
//-- Turn on all the leds
//------------------------------------------------------------------

module leds(output wire LED_BLUE,
            output wire LED_RED,
            output wire LED_GREEN);

assign LED_BLUE = 1'b1;
assign LED_RED = 1'b1;
assign LED_GREEN = 1'b1;

endmodule
