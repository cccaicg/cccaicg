/**
 * Returns the attack coordinates of a unit from a particular coordinate.
 * Also performs random check against the Eliza implementation to make sure
 * the local version is accurate.
 * 
 * @param eliza
 * @param game
 * @param playerName
 * @param unit
 * @param location
 * @return the attack coordinates of a unit from a particular coordinate
 */
public static List<Coordinate> getAttackCoords(Eliza eliza, Game game,
		String playerName, Unit unit, Coordinate location) 
{
	List<Coordinate> attackCoords = new ArrayList<Coordinate>();
	List<Coordinate> attackableCoords = unit.getAttackableCoordinates(location);
	for (Coordinate coord : attackableCoords)
	{
		if (eliza.isAttackable(game, playerName, unit, location, coord))
		{
			attackCoords.add(coord);
		}
	}
	return attackCoords;
}	