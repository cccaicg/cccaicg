/* This is called immediately after onCreate() when the app is started
	 * or after the app comes back from a pause.
	 */
@Override
	protected void onResume() 
{
    super.onResume();
    // Start the game loop
    gameLoopThread = new GameLoopThread(this);
    gameLoopThread.start();
}	