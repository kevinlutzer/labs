module and_gate(

    // Inputs
    input wire BUT,

    // Ouputs
    output wire LED
);

    assign LED = ~BUT;

endmodule