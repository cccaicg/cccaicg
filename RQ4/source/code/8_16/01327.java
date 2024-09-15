/**
 * Get the boolean value associated with a key.
 *
 * @param key   A key string.
 * @return      The truth.
 * @throws   JSONException
 *  if the value is not a Boolean or the String "true" or "false".
 */
public boolean getBoolean(String key) throws JSONException{
    Object o = get(key);
    if (o.equals(Boolean.FALSE) ||
            (o instanceof String &&
            ((String)o).equalsIgnoreCase("false"))) {
        return false;
    } else if (o.equals(Boolean.TRUE) ||
            (o instanceof String &&
            ((String)o).equalsIgnoreCase("true"))) {
        return true;
    }
    throw new JSONException("JSONObject[" + quote(key) +
            "] is not a Boolean.");
}