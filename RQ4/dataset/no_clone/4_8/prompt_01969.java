/**
 * Converts a cursor over the events table to a list of {@link Event}s. If
 * the cursor is empty, will return an empty list.
 *
 * @param eventsCursor
 *            The cursor.
 * @return A list of events.
 */

protected List<Event> getEventsFromCursor(Cursor eventsCursor) 
{
    List<Event> events = new ArrayList<Event>();
    if (eventsCursor != null && eventsCursor.moveToFirst())
    {
        do
        {
            events.add(getEventFromCursor(eventsCursor));
        } while (eventsCursor.moveToNext());
    }
    return events;
}   