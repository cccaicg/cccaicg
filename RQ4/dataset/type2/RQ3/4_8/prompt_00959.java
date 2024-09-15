/**
 * Returns the value associated with the given key, or (byte) 0 if
 * no mapping of the desired type exists for the given key.
 *
 * @param key a String
 * @return a byte value
 */
public byte getByte(String key) 
{
    Object value = map.get(key);
    if (value instanceof Byte)
    {
        return ((Byte) value).byteValue();
    }
    else
    {
        return (byte) 0;
    }
}   