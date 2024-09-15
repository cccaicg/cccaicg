/**
 * Configure the listener for shaking
 * @param threshold
 * 			minimum acceleration variation for considering shaking
 * @param interval
 * 			minimum interval between to shake events
 */
public static void configure(int threshold, int interval){
	AccelerometerManager.threshold = threshold;
	AccelerometerManager.interval = interval;
}