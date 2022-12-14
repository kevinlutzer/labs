module top(
    // input wire clk,
    output wire clk_out
	// input   REFERENCECLK,
	// output  PLLOUTCORE,
	// output  PLLOUTGLOBAL,
	// input   EXTFEEDBACK,
	// input   [7:0] DYNAMICDELAY,
	// output  LOCK,
	// input   BYPASS,
	// input   RESETB,
	// input   LATCHINPUTVALUE,

	// //Test Pins
	// output  SDO,
	// input   SDI,
	// input   SCLK
);

    wire sys_HFOSC;

    SB_HFOSC OSCInst0
    (
        .CLKHFEN   (1'b1),
        .CLKHFPU   (1'b1),
        .CLKHF     (sys_HFOSC)   // 48 MHz
    );

    // assign clk_out = sys_HFOSC;


	SB_PLL40_CORE #(
		.FEEDBACK_PATH("DELAY"),
		.FEEDBACK_PATH("SIMPLE"),
		.FEEDBACK_PATH("PHASE_AND_DELAY"),
		.FEEDBACK_PATH("EXTERNAL"),

		.DELAY_ADJUSTMENT_MODE_FEEDBACK("FIXED"),
		.DELAY_ADJUSTMENT_MODE_FEEDBACK("DYNAMIC"),

		.DELAY_ADJUSTMENT_MODE_RELATIVE("FIXED"),
		.DELAY_ADJUSTMENT_MODE_RELATIVE("DYNAMIC"),

		.PLLOUT_SELECT("GENCLK"),
		.PLLOUT_SELECT("GENCLK_HALF"),
		.PLLOUT_SELECT("SHIFTREG_90deg"),
		.PLLOUT_SELECT("SHIFTREG_0deg"),

		.SHIFTREG_DIV_MODE(1'b0),
		.FDA_FEEDBACK(4'b1111),
		.FDA_RELATIVE(4'b1111),
		.DIVR(4'b0000),
		.DIVF(7'b1111000),
		.DIVQ(3'b000),
		.FILTER_RANGE(3'b000),
		.ENABLE_ICEGATE(1'b0),
		.TEST_MODE(1'b0)
	) uut (
		.REFERENCECLK   (sys_HFOSC   ),
		// .PLLOUTCORE     (PLLOUTCORE     ),
		.PLLOUTGLOBAL   (clk_out   ),
		// .EXTFEEDBACK    (EXTFEEDBACK    ),
		// .DYNAMICDELAY   (DYNAMICDELAY   ),
		// .LOCK           (LOCK           ),
		.BYPASS         (1'b1         ),
		.RESETB         (1'b1         ),
		// .LATCHINPUTVALUE(LATCHINPUTVALUE),
		// .SDO            (SDO            ),
		// .SDI            (SDI            ),
		// .SCLK           (SCLK           )
	);
endmodule