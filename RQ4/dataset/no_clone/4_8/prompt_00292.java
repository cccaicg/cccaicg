/**This method is for the Save Bookmark.*/
public void doSave(RunData data,Context context) 
{
    if (data.get("bookmark") == null)
    {
        data.set("bookmark", new Bookmark());
    }

    Bookmark bookmark = (Bookmark)data.get("bookmark");

    bookmark.setUrl(data.get("url"));
    bookmark.setDescription(data.get("description"));
    bookmark.setTags(data.get("tags"));

    BookmarkService service = new BookmarkService();
    service.save(bookmark);

    data.set("bookmark", bookmark);
    data.set("message", "Bookmark saved successfully");
}   