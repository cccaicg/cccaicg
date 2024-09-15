/**
 * Creates a decimal interval. 
 * @param min the lower bound
 * @param max the upper bound
 * @param openMin if true then the interval excludes the lower bound 
 *                otherwise it includes the lower bound
 * @param openMax if true then the interval excludes the upper bound 
 *                otherwise it includes the upper bound
 */
public DecimalInterval(BigDecimal min, BigDecimal max, 
        boolean openMin, boolean openMax) 
{
    this.min = min;
    this.max = max;
    this.openMin = openMin;
    this.openMax = openMax;
}       