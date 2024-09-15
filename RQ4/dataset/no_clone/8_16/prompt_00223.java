/**
 * Test case 3: Delete a song
 * Test case precondition: Copy a song and rescan the sdcard
 * Verification: The song is deleted from the sdcard and mediastore
 */
@LargeTest
public void testDeleteSong() throws Exception 
{
    String songName = "testDeleteSong";
    String songPath = copySong(songName);
    File songFile = new File(songPath);
    assertTrue("Cannot find the song file", songFile.exists());
    long songId = getSongId(songName);
    assertTrue("Cannot get song id", songId != -1);
    deleteSong(songId);
    assertFalse("The song file is not deleted", songFile.exists());
    songId = getSongId(songName);
    assertTrue("The song is not deleted from mediastore", songId == -1);
}   