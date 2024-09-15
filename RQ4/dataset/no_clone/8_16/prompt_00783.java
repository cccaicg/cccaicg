/**
 * Deflates the polynomial by removing the root.
 * 
 * @param r
 *            double a root of the polynomial (no check made).
 * @return Polynomial the receiver divided by polynomial (x - r).
 */
public Polynomial deflate(final double r) 
{
    int n = degree();
    double[] newc = new double[n];
    for (int i = n; i > 0; i--)
    {
        newc[i - 1] = c[i] - r * c[i - 1];
    }
    return new Polynomial(newc);
}   