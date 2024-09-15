/** 
 * Create a Variant.
 * @param o The wrapped value.
 * @param sig The explicit type of the value, as a dbus type string.
 * @throws IllegalArugmentException If you try and wrap Null or an object which cannot be sent over DBus.
 */
public Variant(T o, String sig) throws IllegalArgumentException 
{
    if (o == null)
        throw new IllegalArgumentException("Null is not a valid variant value");
    if (o instanceof DBusInterface)
        throw new IllegalArgumentException("Objects which implement DBusInterface are not valid variant values");
    this.sig = sig;
    this.o = o;
}   