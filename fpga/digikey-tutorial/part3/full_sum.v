module full_sum(

    // Inputs
    input wire A,
    input wire B,
    input wire C_IN,

    // Ouputs
    output wire S,
    output wire C_OUT
);

    // build sum
    wire A_XOR_B;
    assign A_XOR_B = A ^ B;
    assign S = C_IN ^ A_XOR_B;

    // build carry
    assign C_OUT = (A & B) | (C_IN & A_XOR_B);

endmodule