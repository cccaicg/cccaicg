/**
 * INTERNAL method that returns the device model name with correct capitalization.
 * Taken from: http://stackoverflow.com/a/12707479/1254846
 *
 * @return The device model name (i.e., "LGE Nexus 5")
 */
@NonNull
private static String getDeviceModelName() 
{
    String manufacturer = Build.MANUFACTURER;
    String model = Build.MODEL;
    if (model.startsWith(manufacturer))
    {
        return capitalize(model);
    }
    else
    {
        return capitalize(manufacturer) + " " + model;
    }
}   