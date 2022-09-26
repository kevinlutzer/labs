module and_gate(

    // Inputs
    input wire [1:0] BUT,

    // Ouputs
    output wire [2:0] LED
);
    assign LED[2:0] = 3'b0000;

endmodule