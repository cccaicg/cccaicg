/**
 * @return Optional failure cause, if {@link #isSuccess()} is false
 * @throws IllegalStateException if {@link #isSuccess()} is true
 */
public Optional<Throwable> getError(){
    if (isSuccess()) {
        throw new IllegalStateException("Attempt to retrieve error from successful result");
    }
    return Optional.ofNullable(error);
}