/**
 * Set the minimum length of the formatted string. If this is not set
 * the default is to allow any length.
 * @param minimumLength of the formatted string
 * @return The instance of the builder for chaining.
 */
public FormattedBuilder<T> minimumLength(int minimumLength) 
{
    this.minimumLength = minimumLength;
    return this;
}   