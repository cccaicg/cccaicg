/**
 * Set the maximum length of the formatted string. If this is not set
 * the default is to allow any length.
 * @param maximumLength of the formatted string
 * @return The instance of the builder for chaining.
 */
public FormattedBuilder<T> maximumLength(int maximumLength) 
{
    this.maximumLength = maximumLength;
    return this;
}   