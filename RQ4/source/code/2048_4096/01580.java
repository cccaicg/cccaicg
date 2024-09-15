/**
 * Defines the time that must pass between app crashes to determine that we are not
 * in a crash loop. If a crash has occurred less that this time ago,
 * the error activity will not be launched and the system crash screen will be invoked.
 * The default is 3000.
 */
@NonNull
public Builder minTimeBetweenCrashesMs(int minTimeBetweenCrashesMs){
    config.minTimeBetweenCrashesMs = minTimeBetweenCrashesMs;
    return this;
}