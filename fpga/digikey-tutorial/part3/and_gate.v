module and_gate(

    // Inputs
    input wire [1:0] BUT,

    // Ouputs
    output wire [2:0] LED
);

    assign LED[0] = ~BUT[0];

endmodule