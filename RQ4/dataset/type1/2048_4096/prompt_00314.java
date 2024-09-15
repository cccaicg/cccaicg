/**
 * If set to true and the file exists, the output will be appended to the existing
 * file.
 *
 * @param append defaults to false
 * @return The current instance of the builder
 * @see FlatFileItemWriter#setAppendAllowed(boolean)
 */
public FlatFileItemWriterBuilder<T> append(boolean append) 
{
    this.append = append;
    return this;
}   