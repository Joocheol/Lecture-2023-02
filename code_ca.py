class CrossAttention(BaseAttention):
    def call(self, x, context):
        attn_output = self.mha(
            query=x,
            key=context,
            value=context)

        x = self.add([x, attn_output])
        x = self.layernorm(x)
        return x

    # continued                                                                .