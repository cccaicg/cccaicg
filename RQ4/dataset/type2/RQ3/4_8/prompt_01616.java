/**
 * Find a power of two equal to or greater than the given value.
 * Ie. getPowerOfTwoBiggerThan(800) will return 1024.
 * <P>
 * @see makeTextureForScreen()
 * @param dimension
 * @return a power of two equal to or bigger than the given dimension
 */
public static int getPowerOfTwoBiggerThan(int n) 
{
    int i = 1;
    while (i < n)
        i <<= 1;
    return i;
}   