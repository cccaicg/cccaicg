/**
 * Defines if the error activity must shown the error details button.
 * Set it to true if you want to show the full stack trace and device info,
 * false if you want it to be hidden.
 * The default is true.
 */
@NonNull
public Builder showErrorDetails(boolean showErrorDetails) 
{
    this.showErrorDetails = showErrorDetails;
    return this;
}   