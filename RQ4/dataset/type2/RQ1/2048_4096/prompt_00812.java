/**
 * @return Optional failure cause, if {@link #isSuccess()} is false
 * @throws IllegalStateException if {@link #isSuccess()} is true
 */
public Optional<Throwable> getError() 
{
    if (isSuccess())
    {
        throw new IllegalStateException("Operation was successful");
    }
    return Optional.ofNullable(failureCause);
}   