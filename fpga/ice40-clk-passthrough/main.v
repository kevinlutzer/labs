module main(
    // Input
    output wire led,

    // Clock
    output wire clk,
    output wire clk_out
);
    assign led = clk_out;

    clk_pre_scale clk_pre_scale_i (
        .scaled_clk(clk_out),
        .clk(Clk),
    );

endmodule