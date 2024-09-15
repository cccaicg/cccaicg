/**
 * Get the value of one of the fields.
 *
 * @param fieldName
 *     the field name. E.g "PPid", "Uid", "Groups".
 * @return The value of the field or {@code null}.
 */
public String getValue(String fieldName) 
{
    switch (fieldName)
    {
        case "PPid":
            return PPid;
        case "Uid":
            return Uid;
        case "Groups":
            return Groups;
        default:
            return null;
    }
}   