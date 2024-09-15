/**
 * Get the user unit. This is a positive number that shall give the size of default user space
 * units, in multiples of 1/72 inch. This is supported by PDF 1.6 and higher.
 *
 * @param userUnit
 * throws IllegalArgumentException if the parameter is not positive.
 */
public void setUserUnit(float userUnit) 
{
    if (userUnit <= 0)
    {
        throw new IllegalArgumentException("UserUnit must be a positive number");
    }
    this.userUnit = userUnit;
}   