/**
 * Notify te view is minimized to the DraggableListener
 */
private void notifyMinimizeToListener(){
  if (listener != null) {
    listener.onMinimized();
  }
}