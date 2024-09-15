/**
 * Sets the main activity class that the error activity must launch when a crash occurs.
 * If not set or set to null, the default launch activity will be used.
 * If your app has no launch activities and this is not set, the default error activity will close instead.
 */
@NonNull
public Builder restartActivity(@Nullable Class<? extends Activity> restartActivityClass){
    config.restartActivityClass = restartActivityClass;
    return this;
}