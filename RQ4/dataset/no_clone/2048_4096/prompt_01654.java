// The following methods are used as fallback, when:
// - there is no context (Java threads)
// - the content provider cannot be queried (PackageManagerService)
public static boolean getRestrictedFallback(XHook hook, int uid, String restrictionName, String methodName) 
{
    if (uid > 10000)
        return true; // assume this is a system app

    if (methodName.equals("getRestrictionsChangeListener"))
        return true; // return null

    return false;
}   