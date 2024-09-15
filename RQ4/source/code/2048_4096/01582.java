/**
 * Sets the error activity class to launch when a crash occurs.
 * If null, the default error activity will be used.
 */
@NonNull
public Builder errorActivity(@Nullable Class<? extends Activity> errorActivityClass){
    config.errorActivityClass = errorActivityClass;
    return this;
}