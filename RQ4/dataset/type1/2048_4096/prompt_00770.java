/**
 * Un wrap the obj
 * if obj is {@link Reflector} type, we can call Reflector.get()
 *
 * @param object Object
 * @return real obj
 */
private static Object unwrap(Object object) 
{
    if (object instanceof Reflector)
    {
        return ((Reflector) object).get();
    }
    return object;
}   