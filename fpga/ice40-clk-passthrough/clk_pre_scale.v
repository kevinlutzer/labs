module clk_pre_scale(
    // inputs
    input wire clk,

    // outputs
    output reg scaled_clk
);

    reg [3:0] acc; 

    // accumulator
    always @(posedge clk ) begin
        acc = acc + 7'b1;
    end

    // build the sclaed_clk, flip the value when the accululater fills
    always @(negedge clk ) begin
        if (acc == 4'hf) begin
            scaled_clk = ~scaled_clk;
        end
    end

endmodule