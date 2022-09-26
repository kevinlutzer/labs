module button_counter(
    
    // inputs
    input wire [1:0] but,


    // outputs
    output reg [2:0] led
);

    wire rst;
    wire clk; 
    
    assign rst = ~but[1];
    assign clk = ~but[0];

    always @ (posedge clk or posedge rst) begin
        if (rst == 1'b1) begin
            led <= 3'b111;
        end else begin
            led <= led + 3'b001;
        end
    end

endmodule