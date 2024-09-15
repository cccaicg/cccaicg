/**
 * If set to true, once the step is complete, if the resource previously provided is
 * empty, it will be deleted.
 *
 * @param shouldDelete defaults to false
 * @return The current instance of the builder
 * @see FlatFileItemWriter#setShouldDeleteIfEmpty(boolean)
 */
public FlatFileItemWriterBuilder<T> shouldDeleteIfEmpty(boolean shouldDelete) 
{
    this.shouldDeleteIfEmpty = shouldDelete;
    return this;
}   