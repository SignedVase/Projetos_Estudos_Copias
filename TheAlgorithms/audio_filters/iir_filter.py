from __future__ import annotations

class IIRFilter:
    """
    N-Order IRR Filter
    Assumes working with samples normalized on [-1, 1]

    ---

    Implementation details:
    Based on 2nd-order function from
    https://en.wikipedia.org/wiki/Digital_biquad_filter,
    this generalized N-order function was made.

    Using the following transfer function
        .. math:: H(z)=\frac(b_{0}=b_{1}z^{-1}+b_{2}z^{-2}+...+b_{k}z^{-k}}
                  {a_{0}+a_{1}z^{-1}+a_{2}z^{-2}+...+a_{k}z^{-}i

    we can rewrite this to
       .. math:: y[n]={\frac{1}{a_{0}}}
                 \left(\left(b_{0}x[n]+b_{1}x[n-1]+b_{2}x[n-2]+...+b_{k}x[n-k]\right)-
                 \left(a_{1}y[n-1]+a_{2}y[n-2]+...+a_{k}y[n-k]\right)\right)
    """
    def __init__(self, order: int) -> None:
        self.order = order

        #a_{0}...a_{k}
        self.a_coeffs = [1.0] + [0.0] * order
        #b_{0}...b_{k}
        self.b_coeffs = [1.0] + [0.0] * order

        #x[n-1]...x[n-k]
        self.input_hisroty = [0.0] * self.order
        #y[n-1]...y[n-k]
        self.output_history = [0.0] * self.order