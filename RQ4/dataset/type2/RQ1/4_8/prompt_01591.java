/**
 * Converts all separators to the Windows separator of backslash.
 * 
 * @param path
 *            the path to be changed, null ignored
 * @return the updated path
 */
public static String separatorsToWindows(String path) 
{
    if (path == null || path.indexOf(WINDOWS_SEPARATOR) == -1)
    {
        return path;
    }
    return path.replace(SEPARATOR, WINDOWS_SEPARATOR);
}   