/**
 * Checks that the specified object reference is not {@code null} and
 * throws a customized {@link NullPointerException} if it is.
 *
 * @param obj     the object reference to check for nullity
 * @param message detail message to be used in the event that a {@code
 *                NullPointerException} is thrown
 * @param <T>     the type of the reference
 * @return {@code obj} if not {@code null}
 * @throws NullPointerException if {@code obj} is {@code null}
 */
public static <T> T requireNonNull(T obj, String message) 
{
    if (obj == null)
    {
        throw new NullPointerException(message);
    }
    return obj;
}   