/**
 * Get the actual type arguments a child class has used to extend a generic
 * base class.
 * <p>
 * Child class must be the implementation class of base class.
 * Base class must be a generic class.
 *
 * @param baseClass  the base class
 * @param childClass the child class
 * @return a array type of the raw classes for the actual type arguments.
 */
public static <T> Type[] getActualTypeArguments(
        final Class<T> baseClass, final Class<?> childClass) 
{
    Map<TypeVariable<?>, Type> typeVariableMap =
            GenericTypeReflector.getTypeVariableMap(baseClass);
    Type[] actualTypeArguments =
            GenericTypeReflector.getActualTypeArguments(childClass, typeVariableMap);
    return actualTypeArguments;
}       